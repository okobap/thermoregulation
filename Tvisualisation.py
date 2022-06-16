import matplotlib.pyplot as plt
import numpy as np
import array as arr
import math

# initalising the needed arrays to plot our temperature measurments 
time = arr.array('d', [])
theta1 = arr.array('d', [])
theta2 = arr.array('d', [])
theta3 = arr.array('d', [])
theta4 = arr.array('d', [])



write_to_file_path = "data/" + input("Please enter the name of the experiment : ") + ".txt"

TempDataFile = open(write_to_file_path, "r")
TempDataFile.readline() #to read the first empty line of the .txt file 

#for i in range(10) : 
i = 0
#for line in TempDataFile : 

timeLine = TempDataFile.readline()
t0, d = divmod(float(timeLine), 1) #getting time origin

tempLine = TempDataFile.readline()
while timeLine : 
    print(i)

    # getting time data
    t1, d = divmod(float(timeLine), 1)
    time.append(t1-t0)
    print(t1-t0)

    #getting temperature data
    print(tempLine)
    i += 1
    timeLine = TempDataFile.readline()
    tempLine = TempDataFile.readline()
    #print(TempDataFile.readline())

TempDataFile.close()



                #output_file.write(reply)
               # output_file.close()
  #line = ser.readline()
   # line = line.decode("utf-8") #ser.readline returns a binary, convert to string
   # print(line)
   # output_file.write("\n" + str(time.time()) + "\n")
   # output_file.write(line)











#b = arr.array('d', [2.5, 3.2, 3.3])
#b.append(4.4)

#xpoints = np.array([1, 8])

#zpoints = np.array([3, 20])

#ypoints = np.array([3, 10])

#plt.plot(zpoints, ypoints)
#plt.show()
#plt.plot(xpoints, ypoints)

