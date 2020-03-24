import sys
import os
import sqlite3

def createDb(dir, db):
    tableName = 'files'

    conn = sqlite3.connect(db + '.db')
    curs = conn.cursor()
    command = f'''CREATE TABLE {tableName}
    (ext VARCHAR(5), 
    path VARCHAR(100),
    fname VARCHAR(50))'''

    curs.execute(command)

    for root, dirs, files in os.walk(os.path.normpath(dir)):
        for file in files:
            if file[:1] != '.':
                ext = os.path.splitext(file)[1].replace(".", "")
                if ext == "":
                    ext = None

                command = f'INSERT INTO {tableName} (ext, path, fname) VALUES(?, ?, ?)'
                curs.execute(command, (ext, root.replace('\\', '/'), file))
    
    #curs.execute(f'SELECT * FROM {tableName}')
    #print(curs.fetchall())
    
    conn.commit()
    curs.close()
    conn.close()

def main():
    if len(sys.argv) == 1:
        print('Error: No directory specified')
    elif len(sys.argv) == 2:
        print('Error: No database specified')
    else:
        createDb(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()