import random

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

def generator(wordDict, fname, numWords):
    counter = 0
    currWord = ""
    output = ""
    while counter < numWords:
        if currWord not in wordDict.keys():
            currWord = random.choice(wordDict.keys())
        next = random.choice(wordDict.get(currWord))
        output += currWord
        currWord = next 
        counter += 1
    f = open(fname, "w+")
    f.write(output)
    f.close()

d = train("resume_fun.txt")
generator(d, "text1.txt", 100)

