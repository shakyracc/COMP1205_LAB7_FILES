from pathlib import Path
import os

madLibsFile = open('madlibs.txt')
madLibsFileContent = madLibsFile.read()

madLibsFileContentString = madLibsFileContent.split()

adjective = input("Enter an adjective: ")
firstNoun = input("Enter a noun: ") 
verb = input("Enter a verb: ")
secondNoun = input("Enter a noun: ")


j = -1
isSecondNoun = False

for i in madLibsFileContentString:
    j+=1
    if i == "ADJECTIVE":
        madLibsFileContentString[j] = adjective
        
        continue
    elif i == "NOUN":
        if isSecondNoun == True:
            madLibsFileContentString[j] = secondNoun
        else:
            madLibsFileContentString[j] = firstNoun
            isSecondNoun = True

        print(madLibsFileContentString)
        continue
    elif i == "VERB.":
        madLibsFileContentString[j] = verb + "."
        print(madLibsFileContentString)
        continue

print(" ".join(madLibsFileContentString))


