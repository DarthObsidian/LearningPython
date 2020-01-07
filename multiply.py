print('Enter a matrix a row at a time. End with a blank line.')
data = input(': ')

while data:
    matrixOne = [data]
    data = input(': ')
    if data:
        matrixOne.append(data)

print('Enter a matrix. End with a blank line.')
data = input(': ')

while data:
    matrixTwo = [data]
    data = input(': ')
    if data:
        matrixTwo.append(data)

length = len(matrixOne)
