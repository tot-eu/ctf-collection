#!/usr/bin/python
#Author: Iulian Bancau

import argparse
import hashlib

help_msg = "This app compares a given hash with the hashed value of each password in a given dictionary.\n\n Developed by Iulian Bancau.\n\n https://github.com/tot-eu/ctf-collection"
parser = argparse.ArgumentParser(description = help_msg)
parser.add_argument("-s", "--Search", help = "Search for hash")
parser.add_argument("-d", "--Dictionary", help = "Dictionary file")
args = parser.parse_args()


if args.Search and args.Dictionary:

    file1 = open(args.Dictionary, 'r')
    Lines = file1.readlines()

    def get_hash(arg):
        return hashlib.md5(arg).hexdigest()
    
    count = 0
    for line in Lines:
        count += 1
        string_line = line.strip()
        hash_line = get_hash(string_line)

        if(hash_line == args.Search):
            print("\033[41m[>] Line {}\033[0;32m:  {} -----> {} \033[41m[ Found !!! ]\033[0m".format(count, hash_line, string_line))
            exit()
        else:
            print("[*] Line {}:  {} --> {}".format(count, hash_line, string_line))
else:
    parser.print_help()
