"""Pure structural checks; all authorization decisions are explicitly out of scope.

No AWS integrations, credential handling, I/O, configuration or ambient clock.
Diagnostic reason codes never contain caller-supplied strings or exceptions.
"""

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime
import hashlib
import hmac
import json
import math
import re
from typing import Literal

Status = Literal["STRUCTURALLY_VALID", "REJECTED", "NOT_VERIFIED"]
MAX_JSON_BYTES = 65_536
_SHA256 = re.compile(r"[0-9a-f]{64}\Z", re.ASCII)
_ALLOWED_TYPES = frozenset((str, int, float, bool, dict, list))


@dataclass(frozen=True, slots=True)
class ValidationResult:
    status: Status
    reason: str


def _no_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate key")
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise ValueError("nonfinite number")


def _safe_float(value: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("nonfinite number")
    return number


def _unicode_and_numbers_valid(value: object) -> bool:
    """Check scalar Unicode and nonfinite floats, including nested JSON members."""
    pending = [value]
    while pending:
        current = pending.pop()
        if type(current) is str:
            if any(0xD800 <= ord(char) <= 0xDFFF for char in current):
                return False
        elif type(current) is float:
            if not math.isfinite(current):
                return False
        elif type(current) is list:
            pending.extend(current)
        elif type(current) is dict:
            pending.extend(current.keys())
            pending.extend(current.values())
    return True


def _schema_valid(schema: object) -> bool:
    return (isinstance(schema, Mapping)
            and all(type(key) is str and type(expected) is type and expected in _ALLOWED_TYPES
                    for key, expected in schema.items()))


def decode_json(
    payload: bytes,
    *,
    required_types: Mapping[str, type],
    optional_types: Mapping[str, type] | None = None,
    max_bytes: int = MAX_JSON_BYTES,
) -> tuple[ValidationResult, dict[str, object] | None]:
    """Decode a bounded UTF-8 JSON object and check an *explicit top-level* schema.

    Every nested duplicate key is rejected, but nested field schemas are NOT
    recursively checked. This function never establishes trusted provenance.
    """
    if (type(payload) is not bytes or type(max_bytes) is not int
            or max_bytes < 1 or max_bytes > MAX_JSON_BYTES):
        return ValidationResult("REJECTED", "INVALID_INPUT_BOUNDARY"), None
    if not payload or len(payload) > max_bytes:
        return ValidationResult("REJECTED", "INPUT_SIZE_INVALID"), None
    if not _schema_valid(required_types) or not _schema_valid(
            optional_types if optional_types is not None else {}):
        return ValidationResult("REJECTED", "INVALID_SCHEMA"), None
    optional = optional_types if optional_types is not None else {}
    if set(required_types).intersection(optional):
        return ValidationResult("REJECTED", "INVALID_SCHEMA"), None
    try:
        decoded = json.loads(
            payload.decode("utf-8", errors="strict"),
            object_pairs_hook=_no_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_safe_float,
        )
    except (UnicodeError, ValueError, TypeError, RecursionError):
        return ValidationResult("REJECTED", "INVALID_JSON"), None
    if type(decoded) is not dict:
        return ValidationResult("REJECTED", "OBJECT_REQUIRED"), None
    if not _unicode_and_numbers_valid(decoded):
        return ValidationResult("REJECTED", "INVALID_JSON_SCALAR"), None
    if set(decoded) - (set(required_types) | set(optional)):
        return ValidationResult("REJECTED", "UNKNOWN_FIELD"), None
    if set(required_types) - set(decoded):
        return ValidationResult("REJECTED", "MISSING_FIELD"), None
    for key, value in decoded.items():
        expected = required_types[key] if key in required_types else optional[key]
        if type(value) is not expected:
            return ValidationResult("REJECTED", "INVALID_FIELD_TYPE"), None
    return ValidationResult("STRUCTURALLY_VALID", "STRUCTURE_ONLY"), decoded


def check_sha256(payload: bytes, expected_digest: str) -> ValidationResult:
    """Check literal input bytes against canonical lowercase SHA-256 hex."""
    if type(payload) is not bytes or type(expected_digest) is not str:
        return ValidationResult("REJECTED", "INVALID_DIGEST_INPUT")
    if _SHA256.fullmatch(expected_digest) is None:
        return ValidationResult("REJECTED", "INVALID_DIGEST_FORMAT")
    if not hmac.compare_digest(hashlib.sha256(payload).hexdigest(), expected_digest):
        return ValidationResult("REJECTED", "DIGEST_MISMATCH")
    return ValidationResult("STRUCTURALLY_VALID", "DIGEST_ONLY")


def inspect_clock(clock: Callable[[], datetime]) -> ValidationResult:
    """Validate an injected clock without reading any ambient system time."""
    if not callable(clock):
        return ValidationResult("REJECTED", "CLOCK_REQUIRED")
    try:
        instant = clock()
        if not isinstance(instant, datetime) or instant.tzinfo is None:
            return ValidationResult("REJECTED", "INVALID_CLOCK_VALUE")
        if instant.utcoffset() is None:
            return ValidationResult("REJECTED", "INVALID_CLOCK_VALUE")
    except Exception:
        return ValidationResult("NOT_VERIFIED", "CLOCK_UNAVAILABLE")
    return ValidationResult("STRUCTURALLY_VALID", "CLOCK_SHAPE_ONLY")


def boundary_status(
    structural: ValidationResult | None,
    _unverified_claim: object = None,
) -> ValidationResult:
    """Never promote a caller-supplied record or successful parse into an ALLOW.

    No authority roots, independent signatures, revisions, scopes, replay
    ledger or authenticated adoption events are established in Phase I0.
    Consequently even claims labeled APPROVED/VERIFIED remain NOT_VERIFIED.
    """
    if isinstance(structural, ValidationResult) and structural.status == "REJECTED":
        return ValidationResult("REJECTED", "STRUCTURAL_REJECTION")
    return ValidationResult("NOT_VERIFIED", "NORMATIVE_BASELINE_NOT_VERIFIED")
