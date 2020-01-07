num = input('Enter an interger (Return to quit): ')
numbers = [int(num)]

while num:
    num = input('Enter an interger (Return to quit): ')
    if num:
        numbers.append(int(num))

numbers.sort()
total = sum(numbers)
length = len(numbers)
index = (length-1)//2

if length % 2:
    median = numbers[index]
else:
    median = (numbers[index] + numbers[index+1])/2

print('Numbers:', numbers)
print('sum =', total, ', min =', numbers[0], ', max =', numbers[length-1],
      ', average =', "{:.1f}".format(total/length), ', median =', median)
