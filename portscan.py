from socket import *

target = input('Enter Hostname or IP address: ')
t_IP = gethostbyname(target)

start_port = input("Enter first port in range:\n")
end_port = input("Enter last port in range (max: 65535):\n")

for i in range(int(start_port), int(end_port)+1):
    sock = socket(AF_INET, SOCK_STREAM)

    conn = sock.connect_ex((t_IP, i))

    if (conn == 0):
        print("\033[0;32m[ %d ] port is open (!!!)\033[0m" % (i,))
    sock.close()