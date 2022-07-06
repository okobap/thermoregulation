TempDataFile = open("data/test15.txt" , "r") # opens the .txt file where data was stored
TempDataFile.readline() #to read the first empty line of the .txt file 


timeLine = TempDataFile.readline()


tempLine = TempDataFile.readline()


print(tempLine)

print(tempLine.count("."))

while tempLine.count(".") <= 4 : 
    print(' i am in while loop')
    nextLineThatShouldBeATime = TempDataFile.readline()
    endOfPreviousTempLine = TempDataFile.readline()
    tempLine = tempLine + endOfPreviousTempLine

    print(tempLine)
    print(tempLine.count("."))