import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("my name is becky\nI love coding\nI am a go getter!!")

with open("mydata.txt", encoding="utf-8") as myFile:

    linenum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("line", linenum, )
        wordlist = line.split()
        print("number of words: ", len(wordlist))

        charcount = 0

        for word in wordlist:
            for char in word:
                charcount += 1

        AvgNumChars = charcount/len(wordlist)
        print("average word length: {:.2}".format(AvgNumChars))
        linenum += 1
