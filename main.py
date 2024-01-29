from netmiko import ConnectHandler
from threading import Thread, Lock
from ipaddress import ip_address
from pathlib import Path

lock = Lock()

IPS = Path("ips.csv").read_text().splitlines()
execution = Path("commands.txt").read_text().splitlines()

def is_valid_ip(ip):
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False

def concurrent_back(ip):
    try:
        if not is_valid_ip(ip):
            raise ValueError(f"{ip} is not a valid IP address")

        switch_login = {
            'device_type': "cisco_ios",
            'host': str(ip),
            'username': "changeme",
            'password': "changeme",
            'secret': "changeme",
            'banner_timeout' : 60
        }
        ssh = ConnectHandler(**switch_login)
        ssh.enable()
        output = ssh.send_config_set(execution)
        with open("output.txt", "a") as file:
            file.write(f"{ip}\n{output}\n")
        print(output)
        with lock, open("success.txt", "a") as file:
            file.write(f"{ip}\n")
    except Exception as e:
        with lock, open("errors.txt", "a") as file:
            file.write(f"{e}\n")
        with lock, open("failed_to_connect.txt", "a") as file:
            file.write(f"{ip}\n")

threads = []
for ip in IPS:
    t = Thread(target=concurrent_back, args=(ip,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
