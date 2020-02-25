import sys
import os

def view(fileName, view_size=25):
    #check to see if the file is empty
    if os.path.getsize(fileName) < 1:
        print("Error: specified file is empty")
        return

    with open(fileName, 'r') as f:
        #save positions into a list
        offsets = [0]
        i = 0
        while f.readline():
            i += 1
            if i % view_size == 0:
                f.seek(f.tell())
                offsets.append(f.tell())
        f.seek(0,2)
        fileEnd = f.tell()

        command = ''
        currentPos = 0
        while command != 'q':
            result = []
            #move to the current position
            f.seek(offsets[currentPos])
            
            nextPos = currentPos + 1
            if nextPos == len(offsets):
                nextPos = 0

            #add lines into a list 
            while f.tell() != offsets[nextPos] and f.tell() != fileEnd:
                result.append(f.readline())

            #if the list of lines is too short, lengthen it
            while len(result) < view_size:
                result.append('\n')

            print(''.join(result))
            
            command = input('Command [u,d,t,b,#,q]: ')

            #change the position based on user input
            if command == 'u':
                currentPos -= 1
                if currentPos < 0:
                    currentPos = len(offsets) - 1
            elif command == 'd' or command == '':
                currentPos += 1
                if currentPos >= len(offsets):
                    currentPos = 0
            elif command == 't':
                currentPos = 0
            elif command == 'b':
                currentPos = len(offsets) - 1
            elif command.isdigit():
                currentPos = int(command)
            elif command != 'q':
                print("Error: Invalid command")
            print()

def main():
    if len(sys.argv) > 2:
        view(sys.argv[1], sys.argv[2])
    else:
        view(sys.argv[1])
    
if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Error: No file specified')
    else:
        main()