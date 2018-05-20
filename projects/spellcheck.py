def spellcheck(inputWord,wordCorpus):
    
    # get list of words that share the relatively same size +/- 1 letter
    
    if len(inputWord) == 0:
        print "Please provide a valid word"
        #return "INVALID_ENTRY"
    

    
    
    print "Input word:",inputWord
    #print wordCorpus
    #inputWord = str.split(inputWord)
    word_found = False
    for entry in wordCorpus:
        #print entry
        if entry == inputWord or entry == inputWord[:len(inputWord)-1]:
            print "Valid word found", inputWord
            word_found = True
            break
    if word_found == False:
        print "Not a valid word in dictionary:", inputWord