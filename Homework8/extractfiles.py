import sys
import os
import re
import sqlite3
from zipfile import ZipFile

def extract(file, exp):
        with ZipFile(file, 'r') as zip:
            zipMember = list()
            for item in zip.namelist():
                if re.match(exp, item):
                    zipMember.append(item)
            for member in zipMember:
                print(member)
                zip.extract(path='NewFolder', member=member)

def main():
    if len(sys.argv) == 1:
        print('Error: No zip file specified')
    elif len(sys.argv) == 2:
        print('Error: No expression given')
    else:
        extract(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()