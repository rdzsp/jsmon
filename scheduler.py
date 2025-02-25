import schedule
import time
import subprocess

def run_script():
    print("Executing jsmon.sh...")
    subprocess.run(["bash", "jsmon.sh"], check=True)  # Runs the script using bash

# Schedule the task every 8 hours
schedule.every(8).hours.do(run_script)

print("Scheduler started. Running jsmon.sh every 8 hours.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
