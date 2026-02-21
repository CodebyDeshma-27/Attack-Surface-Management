import subprocess
import yaml

NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"

def run_nmap():
    with open("config/targets.yaml") as f:
        targets = yaml.safe_load(f)["targets"]

    with open("config/scan_profile.yaml") as f:
        args = yaml.safe_load(f)["nmap_arguments"]

    for target in targets:
        command = [
            NMAP_PATH,
            *args.split(),
            "-oX",
            "output/latest_scan.xml",
            target
        ]

        subprocess.run(command, check=True)
