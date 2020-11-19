dictionary_eng = open("/home/kevin/Desktop/ECE 4317 Exercises/ece4317-exercise4/englishdict.txt","r",encoding="cp1252")
results_p1 = open("/home/kevin/Desktop/ECE 4317 Exercises/ece4317-exercise4/results_p1.txt","w")
test_dict = open("/home/kevin/Desktop/ECE 4317 Exercises/ece4317-exercise4/testdict.txt","r")

LEN_ENGDICT = 219492
LEN_TESTDICT = 10

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

    print("word" + "e")

elif(choice == "3"):
    print("Searching for pattern 3")

else:
    print("Select a correct value. Relaunch program")