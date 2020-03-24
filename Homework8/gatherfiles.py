import sys
import os
import sqlite3
from zipfile import ZipFile

def gather(args):
    tableName = 'files'

    conn = sqlite3.connect(args[1] + '.db')
    curs = conn.cursor()

    for item in args[2:]:
        command = f'SELECT * FROM {tableName} WHERE ext = ?'
        curs.execute(command, (item,))
        files = curs.fetchall()
        with ZipFile(f'{item}.zip', 'w') as zip:
            for file in files:
                zip.write(os.path.join(file[1], file[2]))


    curs.close
    conn.close

def main():
    if len(sys.argv) == 1:
        print('Error: No database specified')
    elif len(sys.argv) == 2:
        print('Error: No file type specified')
    else:
        gather(sys.argv)

if __name__ == "__main__":
    main()