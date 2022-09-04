#!/usr/bin/python
#Author: Iulian Bancau

import random
import string

def gen_pass(len):
    passw = ''
    char = string.ascii_letters
    for i in range(len):
        passw += random.choice(char + string.digits)
    return passw

pass_len = int(input('Password length:'))
print(gen_pass(pass_len))
