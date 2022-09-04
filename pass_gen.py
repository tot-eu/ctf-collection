#!/usr/bin/python
#Author: Iulian Bancau

import random
import string

def gen_pass(length):
    pass = ''
    char =  string.ascii_letters
    for i in range(length):
        pass += random.choice(char + string.digits)
    return password

retries = int(input('Password length:'))
print(gen_pass(retries))
