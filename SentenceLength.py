import sys

def main():
    readfile()

def readfile():
    file=sys.argv[1] #get the file from the argument
    f=open(file,"r") #opens the file essay.txt for reading purposes
    report=f.read() #puts the entire file into one sring list
    print("")
    print("Here's the inputed file. We saved the file in the Report variable. A string variable where each of the characters is saved as an element of the list/array")
    print(report)
    print("")
    checkfile(report)
    f.close()
def checkfile(report):
    endofsentence=0
    count=len(report)
    print("")
    print("Here's the length of the file in characters. This is the number of characters in the file.", count)
    print("")
    print("")
    print("This is the first character of the file", report[0])
    print("")
    a=0
    for a in range(0,count):
        if report[a]=='.'or report[a]=='?'or report[a]=='!'or report[a]==';':
            endofsentence+=1

    print("The last character of the file is ", report[count-1])
    print("")
    words=report.split()
    print("")
    print("Now the list of characters has been divided into seperate words and the space has been use as a dilimeter")
    print("The newly created list is now named Words")
    print("So, so far, the number of words in the file is", len(words), "and here\'s the newly created list of words so far")
    print(words)
    print("")

    validwords=0
    testword=0
    b=0
    for a in words:
        testword=words[b]
        numberofcharacters=len(testword)
        print(testword, numberofcharacters)
        if numberofcharacters >=3:
           validwords+=1
        b+=1


    numberwords=len(words)
    print("The number of words is",len(words),"The total number of valid words is", validwords)
    print("The average number of words per sentence is",validwords/endofsentence)


main()