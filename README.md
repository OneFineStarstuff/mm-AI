# Omni-Sentinel Cognitive Execution Environment (CEE)

## Overview
The Omni-Sentinel CEE is a secure, verifiable, and cognitively-aligned execution environment designed for the safe development and deployment of AGI and ASI systems. This repository contains the operational scripts and governance documentation required for daily DevSecOps oversight and long-term regulatory compliance for G-SIFIs (Global Systemically Important Financial Institutions).

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture & Compliance](#architecture--compliance)
- [Operational Scripts](#operational-scripts)
- [Governance Framework](#governance-framework)
- [Key Metrics](#key-metrics)

## Prerequisites
- **Python 3.8+**
- **Hardware Root of Trust:** TPM 2.0 with PCR support.
- **Secure Execution:** Intel SGX or AMD SEV-SNP (Recommended for production).
- **Cloud Infrastructure:** AWS S3 with Object Lock enabled for WORM compliance.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/axiom-spiral/omni-sentinel.git
   cd omni-sentinel
   ```
2. **Environment Setup:**
   Ensure Python 3 is installed and accessible. No external dependencies are required for the core monitor and logger scripts as they use standard libraries for maximum security and minimal attack surface.

## Usage
### Starting the Operational Monitor
To start the 24/7 background monitor with unbuffered output:
```bash
python3 -u omni_sentinel_24h_monitor.py > monitor.log 2>&1 &
```
### Running the PQC Logger
To manually trigger an audit batch commit:
```bash
python3 pqc_worm_logger.py
```

## Architecture & Compliance
The Omni-Sentinel architecture is built on three core pillars:
1. **Cognitive Execution Layer (CEL):** Utilizes TEE/TPM for hardware-rooted attestation.
2. **Governance Layer:** Implements the G-SRI (Global Systemic Risk Index) engine and automated circuit breakers.
3. **Compliance Layer:** Uses S3 WORM storage and Post-Quantum Cryptography (PQC) for immutable audit trails.

### Regulatory Alignment
- **EU AI Act:** Complies with Annex IV requirements for technical documentation and transparency.
- **DORA & NIS2:** Meets operational resilience and cybersecurity reporting standards.
- **Basel III/IV:** Integrated for G-SIFI risk management and supervisory reporting.
- **NIST OSCAL:** Automated reporting for continuous security control assessment.

## Operational Scripts
- **omni_sentinel_24h_monitor.py**: Assesses Systemic Risk (G-SRI), verifies TEE/TPM attestation, and performs health checks.
- **pqc_worm_logger.py**: A post-quantum compliant audit logger using CRYSTALS-Dilithium signatures.

## Governance Framework
- **Roadmap (2026-2035):** See [GOVERNANCE_ROADMAP.md](GOVERNANCE_ROADMAP.md).
- **Reference Architecture:** See [REFERENCE_ARCHITECTURE.md](REFERENCE_ARCHITECTURE.md).
- **Daily Audits:** See [GOVERNANCE_REPORT_20260602.md](GOVERNANCE_REPORT_20260602.md).
- **Global Analysis:** See [AI_SAFETY_GOVERNANCE_ANALYSIS_2026_2030.md](AI_SAFETY_GOVERNANCE_ANALYSIS_2026_2030.md).

## Key Metrics
- **G-SRI Threshold:** < 40.0 (Global Systemic Risk Index)
- **Attestation:** PCR_MATCH=TRUE (Required)
- **Log Integrity:** CRYSTALS-Dilithium signatures with S3 Object Lock.
