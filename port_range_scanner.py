#!/usr/bin/python
#Author: Iulian Bancau

import socket

host = input('Enter Hostname or IP address: ')
t_IP = socket.gethostbyname(host)
print("Select the port range for", t_IP, "scan...")

start_port = input("Enter first port in range:\n")
end_port = input("Enter last port in range (max: 65535):\n")

for i in range(int(start_port), int(end_port)+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    conn = sock.connect_ex((host, i))

    if (conn == 0):
        print("* \033[0;32m[ %d ] port is open!\033[0m" % (i,))
    sock.close()