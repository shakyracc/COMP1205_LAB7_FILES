from pathlib import Path
import time

timeNow = time.strftime("%H:%M:%S").replace(':','_')

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
        continue
    elif i == "VERB.":
        madLibsFileContentString[j] = verb + "."
        continue

print(" ".join(madLibsFileContentString))

# using time to always create a new file with unique file name
newMadLibsFile = open(f'new_mad_libs_{timeNow}.txt','x')

newMadLibsFile.write(" ".join(madLibsFileContentString))

newMadLibsFile.close()
madLibsFile.close()

