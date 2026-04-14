import os
import platform
import subprocess
import json
import time

# ==============================
# UI
# ==============================
def banner():
    os.system("clear" if os.name != "nt" else "cls")
    print("""
🔥 ABHAYA NETSCAN CLI 🔥
----------------------------
Scan WiFi Networks Like a Pro
----------------------------
""")

def loading():
    print("🔍 Scanning", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print("\n")

# ==============================
# LINUX / TERMUX
# ==============================
def scan_termux():
    try:
        output = subprocess.check_output(
            "termux-wifi-scaninfo", shell=True
        ).decode()

        networks = json.loads(output)

        for net in networks:
            print(f"📡 SSID     : {net.get('ssid')}")
            print(f"📶 Signal   : {net.get('level')} dBm")
            print(f"📡 BSSID    : {net.get('bssid')}")
            print(f"📊 Frequency: {net.get('frequency')} MHz")
            print(f"🔐 Security : {net.get('capabilities')}")
            print("-" * 30)

    except Exception as e:
        print("❌ Error:", e)
        print("👉 Install termux-api & give location permission")

# ==============================
# WINDOWS
# ==============================
def scan_windows():
    try:
        output = subprocess.check_output(
            "netsh wlan show networks mode=bssid",
            shell=True
        ).decode(errors="ignore")

        print(output)

    except:
        print("❌ Failed to scan networks")

# ==============================
# LINUX PC (Kali/Ubuntu)
# ==============================
def scan_linux_pc():
    try:
        output = subprocess.check_output(
            "nmcli -f IN-USE,SSID,SIGNAL,SECURITY dev wifi",
            shell=True
        ).decode()

        print(output)

    except:
        print("❌ nmcli not installed")

# ==============================
# MAIN
# ==============================
def main():
    banner()
    loading()

    system = platform.system()

    if system == "Linux":
        # detect termux
        if "ANDROID_ROOT" in os.environ:
            scan_termux()
        else:
            scan_linux_pc()

    elif system == "Windows":
        scan_windows()

    else:
        print("❌ Unsupported OS")

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    main()
