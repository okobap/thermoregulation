TempDataFile = open("data/3006_1001_MaxFreq01.txt", "r") # opens the .txt file where data was stored

actual_TempDataFile = TempDataFile.readlines()
print(actual_TempDataFile)

        
L = actual_TempDataFile[-1][-8:]
print(L)
 