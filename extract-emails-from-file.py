#!/usr/bin/python
#Author: Iulian Bancau

import argparse
import re

help_msg = "Extract emails from file.\n\n Developed by Iulian Bancau.\n\n https://github.com/tot-eu/ctf-collection"
parser = argparse.ArgumentParser(description = help_msg)
parser.add_argument("-f", "--File", help = "File to search in")
args = parser.parse_args()

if args.File:

    f = open(args.File)
    search_in = f.read()

    regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                        "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                        "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

    results = set(regex.findall(search_in))

    emails = ""
    count = len(results)
    for mail in results:
        emails += str(mail[0])+"\n"

    print("==[ " + str(count) + " e-mails found ]==\n")
    print(emails)
    print("==[ " + str(count) + " e-mails found ]==")
else:
    parser.print_help()