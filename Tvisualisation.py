import matplotlib.pyplot as plt
import numpy as np
import array as arr
import math


#This is to be used in order to plot temperature measurements made with the Arduino shield EVAL-CN0391-ARDZ

#The following script should be dowloaded to the Arduino chip in advance C:\Users\BaptisteVauleon\src\projet-thermoregulation\arduino_thermocouple




# initalising the needed arrays to plot our temperature measurments 
time = arr.array('d', [])
theta1 = arr.array('d', [])
theta2 = arr.array('d', [])
theta3 = arr.array('d', [])
theta4 = arr.array('d', [])



#write_to_file_path = "data/" + input("Please enter the name of the experiment : ") + ".txt"

write_to_file_path = "data/2006_1607_MaxCooling01.txt"


TempDataFile = open(write_to_file_path, "r")
TempDataFile.readline() #to read the first empty line of the .txt file 


ierror = 0


timeLine = TempDataFile.readline()
t0, d = divmod(float(timeLine), 1) #getting time origin

tempLine = TempDataFile.readline()

while timeLine and tempLine : 

    #getting temperature data

    tempLine = tempLine.replace(" ", "")
    tempLine = tempLine.replace("\n", "")
    Temps = tempLine.split(",")
    for element in Temps : 
        if len(element) != 5 and len(element) != 4:
            Temps.remove(element)

    if len(Temps) == 4 : 
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

print("corrupted data number : ", ierror)

TempDataFile.close()

fig, ax = plt.subplots()


ax.plot(time, theta1, color='blue', label='T1')
ax.plot(time, theta2, color='black', label='T2')
ax.plot(time, theta3, color='red', label='T3')
ax.plot(time, theta4, color='orange', label='T4')
ax.set_title('Temperatures measurements  - ' + write_to_file_path )
leg = ax.legend()
ax.set_xlabel('time (s)')
ax.set_ylabel(' T (°C)')

plt.show()







  


