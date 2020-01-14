import sys
import re

#read in the file
stringFile = open(sys.path[0] + '\\Strings.txt', 'r')
fullfile = stringFile.read()
stringFile.close

#make all the words lowercase
lowercase = fullfile.lower()
#split the words into a list by everything but a-z and '
splitWords = re.split(r'[^a-z\']', lowercase)

#get the length of the longest word
num = 0
for word in splitWords:
    if len(word) > num:
        num = len(word)

#crate a dictionary key = word value = times word is found, exclude empty strings
words = { word : splitWords.count(word) for word in splitWords if word != ''}
#sorts the dictionary by value
words = {key : value for key, value in sorted(words.items(), key=lambda word: word[1], reverse=True)}

for key, value in words.items():
    name = str(key) + ":"
    #right justify using length of longest word + 1 to account for the added :
    print(name.rjust(num + 1), '{:>5}'.format(str(value)))
