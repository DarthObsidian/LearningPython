import sys


def view(fileName, view_size=25):
    offsets = [0]
   
    with open(fileName, 'r') as f:
        i = 0
        while f.readline():
            i += 1
            if i % view_size == 0:
                offsets.append(f.tell())

        command = ''
        currentPos = 0
        while command != 'q':
            result = ''
            f.seek(offsets[currentPos])
            print(f'starting at pos {f.tell()} in {currentPos}/{len(offsets)}')
            while f.tell() != offsets[currentPos + 1]:
                result += f.readline()
            print(result)
            print(f'ending at {f.tell()}')

            command = input('Command [u,d,t,b,#,q]: ')

            if command == 'u':
                currentPos -= 1
                if currentPos < 0:
                    currentPos = len(offsets) - 1
            elif command == 'd':
                currentPos += 1
                if currentPos >= len(offsets):
                    currentPos = 0
            elif command == 't':
                currentPos = 0
            elif command == 'b':
                currentPos = len(offsets) - 1
            elif command.isdigit:
                currentPos = int(command)
            elif command != 'q':
                print("Error: Invalid command")

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