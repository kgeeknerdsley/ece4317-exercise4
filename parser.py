import difflib
from difflib import SequenceMatcher

dictionary_eng = open("/home/kevin/Desktop/ECE 4317 Exercises/ece4317-exercise4/englishdict.txt","r",encoding="cp1252")
dictionary_danish = open("/home/kevin/Desktop/ECE 4317 Exercises/ece4317-exercise4/danishdict.txt","r",encoding="cp1252")
results_p1 = open("/home/kevin/Desktop/ECE 4317 Exercises/ece4317-exercise4/results_p1.txt","w")
results_p2 = open("/home/kevin/Desktop/ECE 4317 Exercises/ece4317-exercise4/results_p2.txt","w")
test_dict = open("/home/kevin/Desktop/ECE 4317 Exercises/ece4317-exercise4/testdict.txt","r")

LEN_ENGDICT = 219492
LEN_TESTDICT = 10

#like 75% baked idea for testing the difference by one character at any point
#called the Levenshtein Distance, measures the steps it would take to produce a new word by a insertion
#if we find a good pair, the Levenshtein Distance should be 1. Not sure why it always returns 0 so I offset it by one, but we don't have duplicates so w/e
#identical words and a single offset (goal) both produce 0
#https://en.wikipedia.org/wiki/Levenshtein_distance
def levDistance(a, b):
    len_a = len(a)
    len_b = len(b)
    
    if(len_b == 0):
        return len_a
    elif(len_a == 0):
        return len_b
    elif(a[0] == b[0]):
        return levDistance(a[1:len_a-1],b[1:len_b-1])
    else:
        return 1 + levDistance(a, b[1:len_b-1])
        
#how to use it!
res = levDistance("abacinate","abaculus")
print(res)

print("Which pattern do you want to search for?")
print("1) Words that differ by e at the end")
print("2) Words that differ by a single letter")
print("3) Words that differ by a single letter, non-English")
choice = input()

if(choice == "1"):
    print("Searching for additional e words..." + "\n")

    line = 0
    matchCount = 0

    while(line <= (LEN_ENGDICT - 1)):
        currentWord = dictionary_eng.readline() #get the word we're testing
        #print("Testing word: " + currentWord)
        currentWord = currentWord.strip()
        assembled = currentWord + "e"

        for i in range(3):
            if(i == 0):
                nextPos = dictionary_eng.tell() #save the position of the next word to test against

            wordToTest = dictionary_eng.readline() #read a line below
            wordToTest = wordToTest.strip()
            #print("Found word: " + wordToTest)

            if(wordToTest == assembled):
                result = currentWord + "/" + wordToTest+"\n"
                print("Found a match! " + result)
                results_p1.write(result)
                matchCount = matchCount + 1

        line = line+1
        dictionary_eng.seek(nextPos) #reset the scanline to the next non-tested word

    print("Detected "+ str(matchCount) + " matches. Saved to output file")

elif(choice == "2"):
    print("Searching for pattern 2")
    #take length of both words
    #add the lengths together
    #figure out the bigger length
    #if largest length - ratio * (added lengths) / 2 == 1, we found a differ-by-one case

    line = 0
    belowIndex = 0
    matchCount = 0
    firstPass = 0
    nextPos = 0

    seqMatch = SequenceMatcher(None, "a", "aa")

    while(line <= 93): #arbitrary limit
        currentWord = dictionary_eng.readline()
        currentWord = currentWord.strip()
        print("Current word is: " + currentWord)

        seqMatch.set_seq1(currentWord)
        lenCurrent = len(currentWord)

        belowIndex = line+1
        firstPass = 0
        while(belowIndex <= LEN_ENGDICT - 1):
            if(firstPass == 0):
                nextPos = dictionary_eng.tell()
            
            testWord = dictionary_eng.readline()
            testWord = testWord.strip()
            seqMatch.set_seq2(testWord)

            lenTest = len(testWord)

            addedLengths = lenCurrent + lenTest

            if(lenCurrent < lenTest):
                ratio = lenTest - (seqMatch.ratio() * (addedLengths/2))
            else:
                ratio = lenCurrent - (seqMatch.ratio() * (addedLengths/2))

            #print(ratio)
            if(abs(lenCurrent-lenTest) == 1):
                if(ratio == 1.0):
                    print("Found match!")
                    match = currentWord + "/" + testWord + "\n"
                    print(match)
                    results_p2.write(match)

            belowIndex = belowIndex + 1
            firstPass = firstPass + 1
        
        dictionary_eng.seek(nextPos)
        line = line + 1
        print("New line is: " + str(line))
        #print("Current word is: " + currentWord)
    

            
elif(choice == "3"):
    print("Searching for pattern 3")

    #take length of both words
    #add the lengths together
    #figure out the bigger length
    #if largest length - ratio * (added lengths) / 2 == 1, we found a differ-by-one case

    line = 0
    belowIndex = 0
    matchCount = 0
    firstPass = 0
    nextPos = 0

    seqMatch = SequenceMatcher(None, "a", "aa")

    while(line <= 93): #arbitrary limit
        currentWord = dictionary_danish.readline()
        currentWord = currentWord.strip()
        print("Current word is: " + currentWord)

        seqMatch.set_seq1(currentWord)
        lenCurrent = len(currentWord)

        belowIndex = line+1
        firstPass = 0
        while(belowIndex <= LEN_ENGDICT - 1):
            if(firstPass == 0):
                nextPos = dictionary_danish.tell()
            
            testWord = dictionary_danish.readline()
            testWord = testWord.strip()
            seqMatch.set_seq2(testWord)

            lenTest = len(testWord)

            addedLengths = lenCurrent + lenTest

            if(lenCurrent < lenTest):
                ratio = lenTest - (seqMatch.ratio() * (addedLengths/2))
            else:
                ratio = lenCurrent - (seqMatch.ratio() * (addedLengths/2))

            #print(ratio)

            if(ratio == 1.0 and abs(lenCurrent-lenTest) == 1):
                print("Found match!")
                match = currentWord + "/" + testWord + "\n"
                print(match)
                results_p2.write(match)
            
            belowIndex = belowIndex + 1
            firstPass = firstPass + 1
        
        dictionary_danish.seek(nextPos)
        line = line + 1
        print("New line is: " + str(line))
        #print("Current word is: " + currentWord)
    

else:
    print("Select a correct value. Relaunch program")
