import spellcheck

# take all words from alice and store them in memory

aliceFile = open("20k.txt")

wordCorpus = []

for line in aliceFile:
    
    # remove newlines
    line = line.strip().lower()
    
    # get words
    words = line.split(" ")
    #print words
    for word in words:
        if word.isalnum():
            if word not in wordCorpus:
                wordCorpus.append(word)
user_input = raw_input("Enter a sentence you want to spell-check from 20k.txt: ")                

#print wordCorpus
user_input = str.split(user_input)

x = 0
for words in user_input:
    user_input[x] = user_input[x].lower()
    print spellcheck.spellcheck(user_input[x],wordCorpus)
    x +=1
