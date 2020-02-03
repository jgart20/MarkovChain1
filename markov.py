"""
Name: Jeremy Gart
Date: February 2nd, 2020
Purpose: To create a working program that can make sentences based on a given input that mimic the
style/wording of the original, otherwise known as a "Markov Chain".
"""
import random

#function that creates a dictionary of words and the words that follow them based on an inputted source material
def train(filename):
    try:
        f = open(filename, "r")
        lines = f.readlines()
        words = []
        wordDict = {}
        enderList = []
        for line in lines:
            words += line.split()
        for i in range(len(words)-1):
            if wordDict.has_key(words[i]):
                wordDict[words[i]].append(words[i+1])
            else:
                wordDict[words[i]] = [words[i+1]]
            if '.' in words[i] or '!' in words[i] or '?' in words[i] or '...' in words[i]:
                enderList += words[i]
        return wordDict

    except:
         print "File not found. Please try again."

#function that generates text of a given length using the train dictionary above
def generator(wordDict, fname, numWords):
    counter = 0
    currWord = ""
    output = ""
    while counter < numWords:
        if currWord not in wordDict.keys():
            currWord = random.choice(wordDict.keys())
        next = random.choice(wordDict.get(currWord))
        if currWord[0] in "0 1 2 3 4 5 6 7 8 9" or ":" in currWord:
            output += "\n\n"
        output += currWord + " "
        currWord = next 
        counter += 1
    f = open(fname, "w+")
    f.write(output)
    f.close()

#prompting and reading in inputs from the user
trainFile = input("Please enter the file you'd like to train from: ")
d = train(trainFile)
outputFile = input("Please enter the desired name of the generated file: ")
numWords = int(input("Please enter how many words you'd like to generate:"))
generator(d, outputFile, numWords)

