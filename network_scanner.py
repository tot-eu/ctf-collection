import subprocess
host = input('Enter first 3 fields of the IP Address (XXX.XXX.XXX):')
for ping in range(1, 255):
    address = host + "." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print("\033[0;32m", address, "\033[0;42m[ ONLINE ]\033[0m")
    elif res == 2:
        print("\033[0;31m", address, "(offline)\033[0m")
    else:
        print("\033[0;31m", address, "{FAILED}\033[0m")