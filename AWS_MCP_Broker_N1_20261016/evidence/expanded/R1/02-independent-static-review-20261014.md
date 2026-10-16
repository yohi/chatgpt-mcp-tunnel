# AWS MCP Broker v1.1 — Option A Owner Decision Record 独立静的レビュー報告書

- **審査日:** 2026-10-14 (JST)
- **対象:** `DRAFT-AWS-MCP-BROKER-V1.1-OWNER-OPTION-A-20261013`
- **提出物:** `aws-mcp-broker-v1.1-owner-decision-record-option-a(1)(2).md`
- **審査範囲:** 提出文書の真正性ではなく、取得可能な固定資料との**完全性・内部整合・条項差分・承認条件・非退行・残存ブロッカー**の読み取り専用再審査
- **制限:** 審査者の組織的独立性の証明、Owner本人確認、外部の署名済み権威原本との同一性確認、実システム検証は実施していない。AWS/Bitwarden/Cloudflare/Deno/Dockerへの操作、Secret取得、実験、実装、正式承認は実施していない。

## 1. Executive verdict

**正式規範採用の判定: `REVISION_REQUIRED / OWNER_RATIFICATION_BLOCKED`。`NORMATIVE_PASS` は付与しない。**

**3条項の規範改訂候補本文の評価: `CANDIDATE_ACCEPTABLE`。** REQ-009・REQ-046・AC-022の改訂候補本文のハッシュ・原文照合は一致し、固定された安全境界を明白に緩和する差分は発見していない。ただし、Record第4節の非退行要約に、Q40とR4候補REQ-057の「緊急縮小は管理者1名」と衝突し得る、二者承認対象を過度に一般化した文が1か所ある。採用候補本文そのものの問題ではなくRecordの限定修正事項として扱う。

採用意思の記録と正式採用を区別する表示は正しい。Ownerの真正な承認、確定Decision ID、検証可能な日時、権威Baselineの外部原本参照、承認Digest、承認後の別主体によるNormative Reviewが未成立。技術的な安全保証も依然`NOT_PROVEN`である。

## 2. 再計算した完全性・照合証拠

| Evidence | 独立確認 |
|---|---|
| 提出MD SHA-256 | `fe77bbaaed64427778817bdda1e830a3dc0e276fcba2956ec5332be9a7942225` |
| R4原本ZIP SHA-256 | `cd9611654f17d5eee73d47d5d32ce6d94459c24016c2dc3a1a157f90fbd8a15c` — Record記載と一致 |
| R4原本ZIP CRC / manifest | PASS / 14 of 14 MATCH |
| Option A handoff ZIP SHA-256 | `595eb470dd3a6470bb528bf11f732a20929e50e9e3a204cdd3f6e7f6ec464cb9` |
| Option A handoff ZIP CRC / manifest | PASS / 8 of 8 MATCH |
| 提出MD vs handoff内の`00-owner-decision-record-option-a.md` | BYTE-IDENTICAL |
| B1・B2・B3・`08-owner-decision-request.md` | それぞれR4 ZIPとhandoff ZIPのバイト列が一致 |
| R4のB1・B2・B3 SHA-256 | Record記載の3値とそれぞれ一致 |
| 旧条項3件 | `08`の全文から再計算したDigestが一致、かつ対応するB1/B2内の原文と一致 |
| 改訂候補3件 | Record、`08`の改訂候補、handoffの各`adopted-text-*.txt`が一致。SHA-256も3/3一致 |

**採用候補本文のSHA-256**（UTF-8本文のみをstripし終端改行を追加しない）:

- REQ-009: `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9`
- REQ-046: `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931`
- AC-022: `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39`

**重要な限界:** ZIPの内部一致は、B1/B2/B3が署名済みの外部権威原本であることの証明ではない。B3はQ33〜Q40の会話上の決定内容の要約として記載されている。Ownerの本人性・権限・承認日時・署名も、ハッシュの一致だけでは証明できない。

## 3. 3条項の静的技術審査

### 3.1 REQ-009 — CANDIDATE_ACCEPTABLE

1. AWS STS一時認証情報をBroker/AWS Executorの保護領域での必要なAWS署名に限定する。
2. BWS Access TokenをBrokerから独立したSecret Adapter内のSecret Store・実行主体に限定する。
3. 外部サービス用SecretをAdapter内の許可された外部操作に限定し、Broker・AWS Executor・管理UI・AIエージェントへの取得・復号・利用経路を禁止する。
4. 既存AWS IAM長期キーの取得・復号・使用を、Adapterを含むすべての関連構成要素で禁止する。
5. 旧本文の「Broker保護境界」にAdapterを黙示的に含める曖昧さを解消する。

**非退行評価:** 明示的な資格情報公開緩和なし。実効的な境界分離の成立は未実証。

### 3.2 REQ-046 — CANDIDATE_ACCEPTABLE

1. Brokerインストールごとの専用Machine Account/Projectを維持し、Secret取得能力を独立Adapterに分離する。
2. Bitwarden連携初期無効・未承認時のToken配置やAdapter起動を必須としない。
3. 最小権限、保護Projectからの取得拒否、Secret内容だけの差替えを含む取得前強制を要求する。
4. Broker実行/管理主体のBitwarden管理権限と独立Secret Storeアクセスを禁止し、Organization Owner/Admin・特権者経路も検査から除外しない。
5. 二者承認が成立しても既存IAM長期キーの混入を認めない。
6. Password Manager Vaultの非到達性、CLI代理要求による迂回防止、保証不明時のfail-closedを維持する。

**非退行評価:** R3で誤特定された旧第6項の改訂位置と、末尾のPassword Manager/CLI条項の取り残しは、当該全文候補では再発していない。二者承認の実効的な全変更経路強制は未実証。

### 3.3 AC-022 — CANDIDATE_ACCEPTABLE

1. 取得前の真正性・内容不変性・Version拘束・禁止値混入防止を、肯定的Secret取得試験の**前提**にしている。
2. 実IAM長期キーの使用を禁止し、Broker等からのBWS Token・Secret取得拒否および保護Projectへの拒否試験を要求している。
3. 正規に二者承認された禁止値混入も、Secret取得要求前に拒否する条件を明示する。
4. 取得後の秘密内容検査・破棄を「取得前に防いだ」証拠として認めない。

**非退行評価:** 有効化して動かす肯定的試験と、取得前保証不成立時に機能を`BLOCKED`にする安全側停止を区別している。肯定的E2Eが実際に成立したという証拠はない。

## 4. 独立Findingと処置

### ODR-IR-001 — Moderate — Record第4節の二者承認の適用範囲が広すぎる

- **対象:** Decision Record「Explicit decision scope and non-regression」内の「全実効的な権限変更経路には独立二者承認を要求し…」という記載。
- **反例:** Q40の確定決定およびR4規範候補REQ-057は、認可済みの管理者1名によるAdapter緊急停止、Bitwarden連携無効化、Token失効要求、許可リスト縮小、権限取消を許している。Recordの「全権限変更」を逐語的に規範適用すると、この緊急縮小まで2名承認待ちとなり得る。
- **評価:** 権限拡大・高リスクな変更に二者承認を求める趣旨自体は正しい。非退行要約の適用範囲だけが過広で、旧決定との矛盾を生み得る。3つの採用候補本文のDigest変更を必要とするFindingではない。
- **修正条件:** 当該要約を「全実効的な権限拡大・高リスク変更の経路は独立二者承認の強制対象とし、Q40およびR4候補REQ-057が定める認可済み管理者1名による緊急停止・縮小・取消を妨げない。縮小を利用した権限拡大・再有効化は認めない。」など、例外境界を明記した表現へ限定する。

### ODR-IR-002 — Major / Formal blocker — Requirements Ownerの正式採用記録が未成立

- **対象:** Decision metadata、Unresolved evidence、Owner attestation area。
- **事実:** 正式Decision ID、Owner本人性・権限の根拠、独立して監査可能な承認証跡、確定日時、採用本文・Digestへの承認がいずれも未完了。Recordは意図的に`NOT_EFFECTIVE`と表示している。
- **評価:** 草案の虚偽表示はないが、正式な規範改訂として効力を認められない。ChatGPT上の「この判断で進む」という発言だけを、外部の正式承認と同一視してはならない。
- **修正条件:** 正当なOwnerが検証可能な権限・本人性の根拠を伴い、3条項それぞれの**採用全文とDigest**、確定Decision ID、実際の決裁UTC/JST時刻、決裁根拠と監査証跡を確定する。10月13日の意思表明を、事後的に独立認証された承認日時として偽装しない。

### ODR-IR-003 — Moderate / Evidence blocker — 外部権威Baselineのprovenanceが未確定

- **対象:** Decision Record第1・2・6節のB1/B2/B3参照。
- **事実:** R4とhandoff内の4文書はバイト一致する。しかし、別途正式承認された外部B1/B2原本との逐字照合、B3の原決定との照合・権威根拠は独立未確定。
- **評価:** 内部ハッシュの一致と権威原本の真正性は別の保証。
- **修正条件:** 権威ある外部原本の出典、版、保持主体、バイトDigest、署名・決裁等の根拠をOwnerが固定し、差分ゼロを独立検証する。照合不能なら正式レビューでは`BASELINE_INCOMPLETE`の論点として保持する。

## 5. 継続ブロッカー（Decision Recordの新規本文欠陥ではない）

| ID | 重要度 | 残存状態・理由 |
|---|---|---|
| `INT-003` | Critical | Bitwarden Organization Owner/Admin、CI/CD、クラウド特権、Secret Store、独立認可基盤、バックアップ/復元等の**すべての実効変更経路**で独立二者承認が強制されることは未実証。`OPEN / BLOCKING`のまま。 |
| `FEAS-007-C / REQ-045/055` | Major blocker | Secret ID等を変えず禁止値だけを差し込む反例、特に**正規二者承認済み**の禁止値混入を、BWSから値を読み取る前に独立阻止できる保証が未実証。確認不能なら取得を禁止、Adapter連携を`BLOCKED`とする。 |
| `FEAS-Authorization / REQ-053/057` | Major blocker | 独立主体認証、Operation Contract Version/Digestへの拘束、単回使用、`S`送信解放・`D`実送信開始・`C`取消・`R`結果観測の順序を実送信境界で強制する保証は未実証。 |
| `FEAS-001 / FEAS-011 / E2E` | Blocking | AWS長期キーへのfallback防止、環境ごとの独立境界、実Secret未使用の安全な肯定的E2Eが未実証。Deno Deploy、Cloudflare Workers、Docker/Linux、Docker/macOSの各環境で技術証拠が必要。 |
| `REQ-050〜059 / AC-025〜036` | Normative pending | R4候補にとどまり、このRecordによって自動採用されない。AC実行結果は`NOT_EXECUTED`。 |

## 6. 必須修正と次の正規フロー

1. **限定文書修正:** ODR-IR-001の過広な二者承認要約を修正し、Q40の緊急縮小を保全する。REQ-009/REQ-046/AC-022の候補全文および3つのSHA-256は変更不要。
2. **Owner ratification:** ODR-IR-002の正式採用証跡を、Owner本人の真正な決裁として別途固定する。意思表明を公式採用と誤認させない。
3. **External provenance:** ODR-IR-003を独立照合して権威Baselinesを確定する。未検証であればその制限を維持する。
4. **採用後別レビュー:** Ownerが確定した権威原本・採用本文・Digestに対し、新規の独立Normative Reviewを実施し、既存73条項とR4候補の非退行等も照合する。この報告書はその正式なpost-ratification審査の代用ではない。
5. **Feasibilityは別Gate:** `INT-003`などの技術ブロッカーを本報告書で解除しない。独立した許可が得られるまで実証実験・設計承認・実装・本番運用は認可されない。

## 7. Final disposition

- **Document integrity:** PASS
- **3-clause candidate comparison:** PASS / CANDIDATE_ACCEPTABLE
- **Record summary:** LIMITED REVISION REQUIRED (ODR-IR-001)
- **Formal Owner Decision:** PENDING / NOT_EFFECTIVE
- **Independent post-ratification Normative Gate:** NOT_EXECUTED / NORMATIVE_PASS NOT_GRANTED
- **INT-003:** CRITICAL OPEN / BLOCKING
- **Gate S0/S1/C:** NOT_PROVEN
- **Feasibility, Design, Implementation, Production:** NOT_AUTHORIZED

**Overall:** `REVISION_REQUIRED`。Option Aの採用候補本文は維持可能だが、この未認証記録を正式採用の証明として扱わない。
