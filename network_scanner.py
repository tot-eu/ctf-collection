#!/usr/bin/python
#Author: Iulian Bancau
#IF IT IS NOT WORKING, TRY TO CHANGE THE "-t" ATTRIBUTE FROM THE PING COMMAND WITH "-i" OR "-w", depending on the OS YOU USE!!!

import subprocess

first_ip_fields = input('Enter first 3 fields of the IP Address (XXX.XXX.XXX):')
retries = input('Enter number of retries:')
ping_timeout = input('Ping timeout in (seconds):')

for ping in range(1, 256):
    ip_addr = first_ip_fields + "." + str(ping)
    res = subprocess.call(['ping', '-c', retries, '-t', ping_timeout, ip_addr])
    if res == 0:
        print("\033[0;32m", ip_addr, "\033[0;42m[ ONLINE ]\033[0m")
    elif res == 2:
        print("\033[0;31m", ip_addr, "(offline)\033[0m")
    else:
        print("\033[0;31m", ip_addr, "{FAILED}\033[0m")