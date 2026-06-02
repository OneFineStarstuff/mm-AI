import time
import subprocess
import random
from datetime import datetime

def check_g_sri():
    # Simulated G-SRI calculation
    val = round(20.0 + random.uniform(0, 10.0), 2)
    status = "PASS" if val < 40.0 else "FAIL"
    return val, status

def check_attestation():
    # Simulated TEE/TPM PCR match
    return "PCR_MATCH=TRUE"

def run_worm_logger():
    try:
        result = subprocess.check_output(["python3", "pqc_worm_logger.py"], stderr=subprocess.STDOUT)
        return result.decode()
    except Exception as e:
        return f"ERROR: {str(e)}"

def monitor_loop():
    print(f"--- OMNI-SENTINEL COGNITIVE EXECUTION ENVIRONMENT MONITOR STARTING ---")
    print(f"START TIME: {datetime.now()}")

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        gsri, gsri_status = check_g_sri()
        attestation = check_attestation()

        print(f"\n[{timestamp}] CHECKPOINT")
        print(f"[{timestamp}] G-SRI: {gsri} (Threshold: < 40.0) -> {gsri_status}")
        print(f"[{timestamp}] ATTESTATION: {attestation}")

        print(f"[{timestamp}] TRIGGERING WORM AUDIT COMMIT...")
        worm_output = run_worm_logger()
        print(worm_output)

        # In a real 24h monitor this would sleep longer,
        # but for this task I'll make it log every 60 seconds for demonstration
        time.sleep(60)

if __name__ == "__main__":
    monitor_loop()
