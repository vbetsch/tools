# by Victor BETSCH alias vbetsch https://github.com/vbetsch/tools

import os
import argparse
from collections import Counter
from typing import Final, Tuple, List

TITLE_ASCII_ART: Final[str] = """
 ____  _   _ ____  _     ___ ____    _  _____ _____ ____  
|  _ \| | | |  _ \| |   |_ _/ ___|  / \|_   _| ____/ ___| 
| | | | | | | |_) | |    | | |     / _ \ | | |  _| \___ \ 
| |_| | |_| |  __/| |___ | | |___ / ___ \| | | |___ ___) |
|____/ \___/|_|   |_____|___\____/_/   \_\_| |_____|____/ 
"""

CL_BOLD: Final[str] = "\033[01m"
CL_DISABLE: Final[str] = "\033[02m"
CL_RED: Final[str] = "\033[31m"
CL_GREEN: Final[str] = "\033[32m"
CL_RESET: Final[str] = "\033[0m"


DuplicateInfo = Tuple[str, int]


def show_duplicates(duplicates: List[DuplicateInfo]) -> None:
    for filename, count in duplicates:
        print(f"{CL_RED}-> {filename} x{count}{CL_RESET}")


def main() -> None:
    parser = argparse.ArgumentParser(description='Get duplicates files')
    parser.add_argument('--path', type=str, help='Path', required=True)
    args = parser.parse_args()

    print(TITLE_ASCII_ART)
    files = os.listdir(args.path)
    print(f"--------------- {CL_BOLD}files{CL_DISABLE} ---------------{CL_RESET}")
    print(files)

    duplicates = {
        filename.split("(")[0] for filename in files
        if '(' in filename and ')' in filename
    }

    result = [
        (dup, count + 1)
        for dup, count in Counter(duplicates).items()
    ]

    if duplicates:
        print(f"\n--------------- {CL_BOLD}duplicates{CL_DISABLE} ---------------{CL_RESET}")
        show_duplicates(result)
    else:
        print(f"\n{CL_GREEN}OK{CL_RESET}")


if __name__ == '__main__':
    main()
