import sys
import os
import sqlite3

def createDb(dir, db):
    tableName = 'files'

    conn = sqlite3.connect(db + '.db')
    curs = conn.cursor()
    command = f'''CREATE TABLE {tableName}
    (ext VARCHAR(5), 
    path VARCHAR(50),
    fname VARCHAR(20))'''

    curs.execute(command)
    conn.commit

    for root, dirs, files in os.walk(dir):
        for file in files:
            if file[:1] != '.':
                command = f'INSERT INTO {tableName} VALUES({os.path.splitext(files)[1].replace(".", "")}, {root}, {file})'
                curs.execute(command)
                conn.commit
    
    curs.execute('SELECT * FROM files')
    print(curs.fetchall())
    
    conn.close

def main():
    if len(sys.argv) == 1:
        print('Error: No directory specified')
    elif len(sys.argv) == 2:
        print('Error: No database specified')
    else:
        createDb(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()