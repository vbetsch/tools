#!/usr/bin/python
# by Victor BETSCH alias vbetsch https://github.com/vbetsch/Shorts-Projects

import os
import argparse

parser = argparse.ArgumentParser(description='Get duplicates files')
parser.add_argument('--path', type=str, help='Path (required)')
args = parser.parse_args()

CL_BOLD = '\033[01m'
CL_DISABLE = '\033[02m'
CL_RED = '\033[31m'
CL_GREEN = '\033[32m'
CL_RESET = '\033[0m'


def show_duplicates(duplicates):
    for duplicate in duplicates:
        print(f"{CL_RED}-> {duplicate[0]} x{duplicate[1]}{CL_RESET}")


def run():
    print("""
 ____  _   _ ____  _     ___ ____    _  _____ _____ ____  
|  _ \| | | |  _ \| |   |_ _/ ___|  / \|_   _| ____/ ___| 
| | | | | | | |_) | |    | | |     / _ \ | | |  _| \___ \ 
| |_| | |_| |  __/| |___ | | |___ / ___ \| | | |___ ___) |
|____/ \___/|_|   |_____|___\____/_/   \_\_| |_____|____/ 
    """)
    files = os.listdir(args.path)
    print(f"--------------- {CL_BOLD}files{CL_DISABLE} ---------------{CL_RESET}")
    print(files)

    duplicates = list(map(lambda x: x.split("(")[0],
                          filter(lambda y: y if y.__contains__("(") and y.__contains__(")") else None, files)))
    result = [(dup, duplicates.count(dup) + 1) for dup in set(duplicates)]

    if duplicates:
        print(f"\n--------------- {CL_BOLD}duplicates{CL_DISABLE} ---------------{CL_RESET}")
        print(show_duplicates(result))
    else:
        print(f"\n{CL_GREEN}OK{CL_RESET}")


run()
