# Contributing to Omni-Sentinel

Thank you for your interest in the Omni-Sentinel project. As this repository manages critical governance and containment infrastructure for AGI/ASI systems, we maintain high standards for contributions.

## Governance & Audit Requirements
All code contributions must adhere to the following:
1. **Safety First:** No change should compromise the G-SRI engine or circuit breaker logic.
2. **Formal Verification:** Changes to containment logic must be accompanied by TLA+ or similar formal verification updates.
3. **PQC Compliance:** All telemetry and logging changes must use CRYSTALS-Dilithium compatible signatures.
4. **Audit Trail:** Every PR must include a summary of its impact on the Global Systemic Risk Index.

## Process
1. **Discuss:** Open an issue to discuss significant changes before starting work.
2. **Fork & Branch:** Create a feature branch from `main`.
3. **Test:** Run the operational monitor (`omni_sentinel_24h_monitor.py`) and verify that your changes do not trigger false positives or suppress telemetry.
4. **Commit:** Use descriptive commit messages.
5. **PR:** Submit a Pull Request. A maintainer will review your code for safety and compliance.

## Coding Standards
- **Python:** Follow PEP 8.
- **Documentation:** Update relevant MD files (REFERENCE_ARCHITECTURE, ROADMAP, etc.) if your change affects system design.
- **Security:** Avoid adding external dependencies. If a dependency is necessary, it must be vetted for supply chain risks.
