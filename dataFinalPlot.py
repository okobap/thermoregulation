
import matplotlib.pyplot as plt
import numpy as np
import array as arr
import math

def plotingAndSaving(nameExp, write_to_file_path) : 
    time = arr.array('d', [])   ## initalising the needed arrays to plot our temperature measurments 
    theta1 = arr.array('d', [])
    theta2 = arr.array('d', [])
    theta3 = arr.array('d', [])
    theta4 = arr.array('d', [])



    TempDataFile = open(write_to_file_path, "r") # opens the .txt file where data was stored
    TempDataFile.readline() #to read the first empty line of the .txt file 


    ierror = 0 # sets the corrupted data counter to 0. Corrupted data comes from stroing data that was being writen by the Arduino chip while this script was inspecting the serial port


    timeLine = TempDataFile.readline()
    t0, d = divmod(float(timeLine), 1) #getting time origin

    tempLine = TempDataFile.readline()

    while timeLine and tempLine : # runs until all the .txt file was run through

        #getting temperature data

        while tempLine.count(".") <= 3 and tempLine[-8:] != "The End.": 
            nextLineThatShouldBeATime = TempDataFile.readline()
            endOfPreviousTempLine = TempDataFile.readline()
            tempLine = tempLine + endOfPreviousTempLine
           
       
        tempLine = tempLine.replace(" ", "")
        tempLine = tempLine.replace("\n", "")

        Temps = tempLine.split(",")
        for element in Temps : 
            if len(element) != 5 and len(element) != 4 :
                Temps.remove(element) # checks for corrupted data. Typically should look like an absent or partial temperature measurement that should normally look like '24.03'

        if len(Temps) == 4 and timeLine != '': # if one temperature measurement is corrupted then the all set is deleted
            theta1.append(float(Temps[0]))
            theta2.append(float(Temps[1]))
            theta3.append(float(Temps[2]))
            theta4.append(float(Temps[3]))

            # getting time data
            t1, d = divmod(float(timeLine), 1)
            time.append(t1-t0)
        

        else : 

            ierror += 1
    
        # moving on to the next lines 
        timeLine = TempDataFile.readline()
        tempLine = TempDataFile.readline()

    print("\nnumber of points : ", len(theta1))
    print("corrupted data number : ", ierror)

    TempDataFile.close()


    fig, ax = plt.subplots()


    ax.plot(time, theta1, color='blue', label='T1')
    ax.plot(time, theta2, color='black', label='T2')
    ax.plot(time, theta3, color='red', label='T3')
    ax.plot(time, theta4, color='orange', label='T4')
    ax.set_title('Temperatures measurements  - ' + nameExp )
    leg = ax.legend()
    ax.set_xlabel('time (s)')
    ax.set_ylabel(' T (°C)')
    plt.savefig("data/" + nameExp + ".png")

    plt.show()

    print("\nSee you around !")


#plotingAndSaving('0607_1035_NewCube3', "data/0607_1035_NewCube3.txt")