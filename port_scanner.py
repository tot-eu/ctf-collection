#!/usr/bin/python
#Author: Iulian Bancau

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("Enter Hostname or IP address:\n")

start_port = input("Enter port:\n")

def port_scan(port):
    if sock.connect_ex((host,port)):
        print("\033[0;31m[ %d ] port is closed\033[0m" % (port))
    else:
        print("\033[0;32m[ %d ] port is open (!!!)\033[0m" % (port))
        
port_scan(int(start_port))
