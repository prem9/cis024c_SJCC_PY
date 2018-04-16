import string

aliceFile = open("aliceText.txt")

wordCounts = {}

for line in aliceFile:
    words = line.strip().split()

    for word in words:
        
        word = word.lower()
        
        invalid_letter = False
        for letter in word:
            
            if letter not in string.letters:
                invalid_letter = True
                break
                
        if invalid_letter == True:
            continue
        
                
        if wordCounts.get(word) == None:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
def getEditDistance(w):
    
    bestMatch = []
    minCost = None
    
    for word in wordCounts:
    
        cost = 0
        rangeLen = min(len(w),len(word))
        
        for i in range(rangeLen):
            
            if w[i] == word[i]:
                continue
            else:
                cost += 1
                
        cost += abs(len(w) - len(word))
        
        if minCost == None or cost < minCost:
            minCost = cost
            bestMatch = []
            bestMatch.append(word)
            
        if minCost == cost:
            bestMatch.append(word)
            
    return (minCost,bestMatch)