def train(filename):
    try:
        file = open(filename, read)
        lines = file.readlines()
        words = []
        wordDict = {}
        enderList = []
        for line in lines:
            words += line.split()
        for i in range(len(words)-1):
            if wordDict.has_key(words[i]):
                wordDict[words[i]].append(words[i+1])
            else wordDict[words[i]] = [words[i+1]]
            if '.' in words[i] or '!' in words[i] or '?' in words[i] or '...' in words[i]:
                

    except:
         print "File not found. Please try again."

def generate