# Omni-Sentinel Reference Architecture

## 1. Cognitive Execution Layer
- **TEE (Trusted Execution Environment):** Intel SGX / AMD SEV-SNP.
- **TPM:** Hardware-rooted identity for PCR (Platform Configuration Register) matching.

## 2. Governance Layer
- **G-SRI Engine:** Real-time risk scoring based on model outputs and resource consumption.
- **Circuit Breaker:** Automated kill-switch for threshold violations.

## 3. Compliance & Audit Layer
- **WORM Storage:** AWS S3 with Object Lock.
- **PQC Logger:** Post-quantum signatures (Dilithium) for all log entries.
- **ZKP Registry:** Zero-Knowledge Proof registry for public verification of private audits.

## 4. Connectivity
- **EAIP:** Enterprise AI Agent Interoperability Protocol for secure inter-agent communication.
