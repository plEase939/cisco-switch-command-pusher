# cisco-switch-command-pusher
A simple python script to Login and push your pre-configured set of commands to 100s or 1000s of Cisco switches.

First open main.py and enter your Cisco switch login credentials. Can be your local login or TACACS login.  Your enable password should be in "secret"

Second open commands.txt and you may completely rewrite this file with your commands. The command se initially send directly to config terminal. If you want your commands to not initially push to config terminal then simply enter first line as exit

Third enter your list of IP addresses to ips.csv file. Make sure there are no extra spaces beside the IP address line.

Thats it! now you may simply execute this program and the program will login to each switch concurrently and push commands.
