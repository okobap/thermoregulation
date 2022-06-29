import time
import matplotlib.pyplot as plt
import numpy as np


def update_line(line1, new_x, new_y):
    line1.set_xdata(np.append(line1.get_xdata(),[new_x]))
    line1.set_ydata(np.append(line1.get_ydata(),[new_y]))
    
    # Rescale axes limits
    ax.relim()
    ax.autoscale()

    figure.canvas.draw()
    figure.canvas.flush_events()
    


def livePloting(nameExp, write_to_file_path, listen_running, number_of_lines_in_Tempfile):



    time.sleep(10)
    
    timeline = []
    theta1 = []
    theta2 = []
    theta3 = []
    theta4 = []

    plt.ion()

    ax: plt.Axes
    figure, ax = plt.subplots(figsize=(10, 8))
    (line1,) = ax.plot(timeline, theta1, color='blue', label='T1')
    (line2,) = ax.plot(timeline, theta2, color='black', label='T2')
    (line3,) = ax.plot(timeline, theta3, color='red', label='T3')
    (line4,) = ax.plot(timeline, theta4, color='orange', label='T4')

    ax.set_title('Temperatures measurements  - ' + nameExp )
    leg = ax.legend()

    ax.autoscale(True)

    plt.xlabel("time (s)")
    plt.ylabel("T (°C)")


    while listen_running : 

        TempDataFile = open(write_to_file_path, "r") # opens the .txt file where data was stored

        actual_number_of_lines = len(TempDataFile.readlines())

        if (actual_number_of_lines != number_of_lines_in_Tempfile) and (actual_number_of_lines % 2 == 1) :

            TempDataFile.readline() #to read the first empty line of the .txt file 
            timeLine = TempDataFile.readline()
            t0, d = divmod(float(timeLine), 1) #getting time origin

            timeLine = TempDataFile.readline()[-2]
            tempLine = TempDataFile.readline()[-1]

            t1, d = divmod(float(timeLine), 1)

            durée = t1 - t0

            tempLine = tempLine.replace(" ", "")
            tempLine = tempLine.replace("\n", "")
            Temps = tempLine.split(",")
            for element in Temps : 
                if len(element) != 5 and len(element) != 4 :
                    Temps.remove(element) # checks for corrupted data. Typically should look like an absent or partial temperature measurement that should normally look like '24.03'

            if len(Temps) == 4 : # if one temperature measurement is corrupted then the all set is deleted
                update_line(line1, durée, Temp[0])
                update_line(line2, durée, Temp[1])
                update_line(line3, durée, Temp[2])
                update_line(line4, durée, Temp[3])
        
        time.sleep(1)


        
        TempDataFile.close()
