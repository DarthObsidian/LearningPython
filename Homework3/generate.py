def produce (input):
    i = 0
    while i < len(input):
        if(input[i].isdigit()):
            yield input[i+1]*(int(input[i]) + 1)
            i += 2
        else:
            yield input[i]
            i += 1

def consume(generator):
    result = ''
    for word in generator:
        for char in word:
            result += char
            if (len(result) + 1) % 4 == 0:
                result += ' '
    print(result)

def main():
    p = produce('A2B5E3426FG0ZYW3210PQ89R')
    for s in p:
        print(s, end=' ')
    print()

    consume(produce('A2B5E3426FG0ZYW3210PQ89R'))

if __name__ == "__main__":
    main()