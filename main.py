#Importing Dependencies
from netmiko import ConnectHandler
from threading import Thread, Lock
import csv
import time


IPS =[]  #empty list
lock = Lock() 
execution = [] #empty list

#Open ips.csv and append each line to IPS list
with open("ips.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        IPS.append(row[0])

#print List and read and append commands from commands.txt commands will be directly enter to config t, enter first line as exit if you don't want to start with config t
print(IPS)
with open("commands.txt", "r") as file:
    reader = file.readlines()
    for row in reader:
        execution.append(row.splitlines()[0])

def concurrent_back(ip):
    try:
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
        with open("output.txt", "a+") as file:
            file.write(ip + "\n" + output + "\n")
            file.close()
        print(output)
        with open("success.txt", "a") as file:
            lock.acquire()
            file.write(str(ip) + "\n")
            file.close()
            lock.release()
    except Exception as e:
        lock.acquire()
        with open("errors.txt", "a") as file:
            file.write(str(e) + "\n")
            file.close()
        with open("failed_to_connect.txt", "a") as file:
            file.write(str(ip) + "\n")
            file.close()
        lock.release()


threads = []
for ip in IPS:
    t = Thread(target=concurrent_back, args=(ip,))
    t.start()
    threads.append(t)

#Wait Pending Threads to complete their task. When all workers finish their task then program is terminated
for t in threads:
    t.join()
