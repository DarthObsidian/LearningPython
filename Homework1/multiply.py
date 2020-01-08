#first matix must have the same number of columns as the second matrix has rows
#if this isn't true it is an invalid matrix multiplication

print('Enter a matrix a row at a time. End with a blank line.')
userInput = '0'
matrixOne = []

while userInput:
    userInput = input(': ')
    if userInput:
        nums = list(map(int, userInput.split()))
        matrixOne.append(nums)

print('\nEnter a matrix. End with a blank line.')
userInput = '0'
matrixTwo = []

while userInput:
    userInput = input(': ')
    if userInput:
        nums = list(map(int, userInput.split()))
        matrixTwo.append(nums)

if len(matrixOne) < 1 or len(matrixOne[0]) != len(matrixTwo):
    print('\nProvided matrices are not compatible.')
else:
    finalMatrix = []

    i = 0
    while i < len(matrixOne):
        row = []
        j = 0
        while j < len(matrixTwo[0]):
            k = 0
            while k < len(matrixTwo):
                result = matrixOne[i][k] * matrixTwo[k][j]
                k += 1
                result2 = matrixOne[i][k] * matrixTwo[k][j]
                row.append(result + result2)
                k += 1
            j += 1
        i += 1
        finalMatrix.append(row)

    print('\nResult:')
    for item in finalMatrix:
        for num in item:
            print('{:>4}'.format(str(num)), end= '')
        print('')

input('Press any key to exit...')
