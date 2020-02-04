import sys
import random
import itertools

#gets all the 6 letter and under words from the words.txt file
def GetWords():
    wordFile = open(sys.path[0] + '\\words.txt', 'r')
    wordlist = [word.strip() for word in wordFile if len(word.strip()) <= 6 if len(word.strip()) > 2]
    wordFile.close()

    return wordlist

#returns a list of words of a given size from the given list
def GetSizedWords(num, wordList):
    sizedList = [word for word in wordList if len(word) == num]
    return sizedList

#returns a randomly picked word from a given list
def ChooseWord(wordList):
    num = random.randint(0, len(wordList)-1)
    return wordList[num]

#jumbles the provided word
def JumbleWord(word):
    w = list(word)
    random.shuffle(w)
    return ''.join(w)

#returns all valid words whos length is between 2 and the length of the given word
def GetValidWords(word, wordList):
    permuts = set()
    i = len(word)
    while i > 2:
        permut = itertools.permutations(word, i)
        for item in permut:
            permuts.add(''.join(item))
        i -= 1

    vaildWords = [combo for combo in permuts
                        for item in wordList
                        if combo == item]

    vaildWords.sort()
    vaildWords.sort(key=len)
    return vaildWords

def main():
    masterWords = GetWords()
    baseWord = ''

    #check for user defined word
    if len(sys.argv) == 2:
        baseWord = sys.argv[1]
    else:
        maxSizeWords = GetSizedWords(6, masterWords)
        baseWord = ChooseWord(maxSizeWords)

    #jumble the base word
    jumbledWord = JumbleWord(baseWord)

    #get all the valid words
    validWords = GetValidWords(baseWord, masterWords)

    #initialize user-found words
    foundThreeWords = list()
    foundFourWords = list()
    foundFiveWords = list()
    foundSixWords = list()

    #initialize the number of words left to be found
    numSixLeft = 0
    numFiveLeft = 0
    numFourLeft = 0
    numThreeLeft = 0
    for word in validWords:
        size = len(word)
        if size == 6:
            numSixLeft += 1
        elif size == 5:
            numFiveLeft += 1
        elif size == 4:
            numFourLeft += 1
        elif size == 3:
            numThreeLeft += 1

    print('\nTEST: base word is', baseWord)

    #the actual game
    while True:
        #saves all the found words into a list for readability later
        foundWords = foundThreeWords + foundFourWords + foundFiveWords + foundSixWords
        #ends the game if the use has found all the words
        if len(foundWords) == len(validWords):
            print("CONGRATULATIONS! You've won!")
            break

        #show how many of each word user has left and which ones user already guessed
        print('\n'+jumbledWord + ':\n')
        print(numThreeLeft, '3-letter words left.')
        print(foundThreeWords)
        print(numFourLeft, '4-letter words left.')
        print(foundFourWords)
        print(numFiveLeft, '5-letter words left.')
        print(foundFiveWords)
        print(numSixLeft, '6-letter words left.')
        print(foundSixWords)

        #wait for input
        userInput = input('\nEnter a guess: ').strip()

        #end the game if input is q
        if userInput == 'q':
            break
        #if the inpus if valid and not already found
        elif userInput in validWords and userInput not in foundWords: 
            print('Correct!')
            size = len(userInput)
            if size == 6:
                foundSixWords.append(userInput)
                numSixLeft -= 1
            elif size == 5:
                foundFiveWords.append(userInput)
                numFiveLeft -= 1
            elif size == 4:
                foundFourWords.append(userInput)
                numFourLeft -= 1
            elif size == 3:
                foundThreeWords.append(userInput)
                numThreeLeft -= 1
        #if the input is incorrect or already found
        else:
            print('Incorrect or already guessed')
    
    #at the end of the game print all the valid words
    print(validWords)

    
if __name__ == "__main__":
    main()
