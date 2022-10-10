#!/usr/bin/python
#Author: Iulian Bancau
import requests
import argparse

help_msg = "Simple web enumeration tool.\n\n Developed by Iulian Bancau.\n\n https://github.com/tot-eu/ctf-collection"
parser = argparse.ArgumentParser(description = help_msg)
parser.add_argument("-u", "--URL", help = "Base URL without the end slash")
parser.add_argument("-d", "--Dictionary", help = "Dictionary file")
args = parser.parse_args()

if args.URL and args.Dictionary:
    dict = open(args.Dictionary, 'r')
    URLs = dict.readlines()

    def request(path):
        base_url = args.URL
        url = base_url + '/' + path
        try:
            response = requests.get(url)
            if response.status_code != 404:
                if response.status_code == 200:
                    print(f'\033[0;42m[ {response.status_code} ]\033[0m:\t{url}')
                else:
                    print(f'\033[41m[ {response.status_code} ]\033[0m:\t{url}')
        except Exception as e:
            pass

    for i in URLs:
        request(i.strip('\n'))

else:
    parser.print_help()
