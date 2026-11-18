# Portfolio verification - 19 November 2026 (Asia/Singapore)

This records local portfolio checks, distinct from historical coursework evaluation. Original coursework folders were treated as read-only. No remote repository was created or changed.

| Check | Status | Scope |
| --- | --- | --- |
| Python syntax and default notebook inspection | Passed | Python files parsed; all three public notebooks executed only in the default outer inspection mode, without ML imports, fitting or evaluation. |
| Relative Markdown links | Passed | Repository documentation resolves locally; upstream README links resolve to pinned external locations. External links were not exhaustively fetched. |
| File and Git-index review | Passed | Explicit public manifest; no inherited history or remotes; private generated fixtures ignored. |
| Privacy/secret scan | Passed within scan scope | All public-file bytes, notebook sources and checkpoint metadata scanned for known credentials, private paths, student ID and common token/private-key formats. No matches. This is a bounded review, not a formal security assessment. |
| Visual assets | Passed within scope | Fraud/Fashion confusion matrices and hardware photograph inspected; image files decoded and metadata checked. No fabricated UI screenshots. |
| Original-source preservation | Passed | 3,513 baseline source/evidence/teaching files rehashed unchanged; original runtime data, archived history and working executable were not modified or used as test inputs. |
| Fresh dependency installation | Not executable in available setup | Checks used retained dependencies where required; clean installation and full platform portability were not established. |


## OIDS-specific checks

`python tools/verify_saved_results.py` passed using the standard library. It verifies fraud confusion-count arithmetic, Fashion-MNIST validation ranking and selected checkpoint/dataset hashes, and the stroke summary's confusion-count arithmetic. All five Fashion checkpoint hashes were also checked against their saved summaries. Saved PR-AUC/loss values were cross-checked with existing records, not recomputed from new inference.

No training or final-test scoring was run. The source notebooks' original embedded outputs are excluded from this public copy; aggregate records and selected original plots preserve the reported evidence. Exact training reproduction and an independent statistical reanalysis are unverified. Missing fraud/stroke data redistribution rights were handled by excluding those datasets and record-level outputs.

Git whitespace check: retained historical CSV/model-summary EOF blank lines and original upstream driver formatting produce nonblocking warnings. Source/evidence content is preserved; text line endings in public copies are normalised to LF. See the local whitespace logs.
