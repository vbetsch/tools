# by Victor BETSCH alias vbetsch https://github.com/vbetsch/tools

import os
import argparse

parser = argparse.ArgumentParser(description='Get duplicates files')
parser.add_argument('--path', help='Path (required)', required=True, default="/home", type=str)
parser.add_argument('--files', help='Show files', required=False, default=False)
args = parser.parse_args()

CL_BOLD = '\033[01m'
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

    if args.files:
        print(f"--------------- {CL_BOLD}files{CL_RESET} ---------------{CL_RESET}")
        print(files)

    duplicates = list(map(
        lambda x: x.split("(")[0] + x.split(")")[1]
        if "(" in x and ")" in x else x,
        filter(
            lambda y: y
            if "(" in y and ")" in y else None,
            files)
    )
    )
    result = [(dup, duplicates.count(dup) + 1) for dup in set(duplicates)]

    if duplicates:
        print(f"\n--------------- {CL_BOLD}duplicates{CL_RESET} ---------------{CL_RESET}")
        print(show_duplicates(result))
        print(f"{CL_RED}Found {CL_BOLD}{len(result)}{CL_RESET}{CL_RED} results{CL_RESET}")
    else:
        print(f"\n{CL_GREEN}OK{CL_RESET}")


if __name__ == '__main__':
    run()
