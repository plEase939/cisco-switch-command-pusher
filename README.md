# cisco-switch-command-pusher

Run pip install netmiko

A simple python script to Login and push your pre-configured set of commands to 100s or 1000s of Cisco switches.

First open main.py and enter your Cisco switch login credentials. Can be your local login or TACACS login.  Your enable password should be in "secret"

Second open commands.txt and you may completely rewrite this file with your commands. The command se initially send directly to config terminal. If you want your commands to not initially push to config terminal then simply enter first line as exit

Third enter your list of IP addresses to ips.csv file. Make sure there are no extra spaces beside the IP address line.

Thats it! now you may simply execute this program and the program will login to each switch concurrently and push commands.

Here's a breakdown of its functionality:
1.  It reads a list of IP addresses from a CSV file (ips.csv). Each IP address corresponds to a Cisco device on your network.

2.  It also reads a list of commands from a text file (commands.txt). These commands are Cisco IOS commands that you want to execute on each device.

3.  The script then creates a separate thread for each device. In each thread, it establishes an SSH connection to the device using the netmiko library, which is a Python library for interacting with network devices.

4.  Once connected, it sends the list of commands to the device and captures the output.

5.  The output from each device is appended to a file (output.txt), along with the IP address of the device.

6.  If the commands are executed successfully, the IP address of the device is written to another file (success.txt).

7.  If an exception occurs during the execution of the commands, the script acquires a lock and logs the error.

8.  In summary, this script allows you to automate the process of executing commands on multiple Cisco devices and logging the results.


You are free to modify this script as per your need.

You are solely responsible for the commands you push using this script. 
