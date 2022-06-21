import serial
import time
import threading

import matplotlib.pyplot as plt
import numpy as np
import array as arr
import math
import os
import os.path
from os import path




#This is to be used in order to launch an Temperature monitoring experiment. The total duration and period between temperature measurements are to be set via the terminal while the code is running. 
#You will also have to enter the 'name' of the port your are using to communicate with the Arduino chip on which the thermocouples are installed. This name should typically look like 'COM3'.

#After having collected all the data you will be invited to press enter, then the data will be ploted and the according figure saved with the .text data file

#At any time you should be able to shut down the communication with the Arduino chip by entering 'exit!' in the terminal when 'Arduino>>' is showing. 

#Be aware that when you shut down the communication with the Arduino chip, the code on the chip is still running. To completely shut down the chip and until a better solution you will have to unplug the alimentation of the chip

#The following script should be dowloaded to the Arduino chip in advance C:\Users\BaptisteVauleon\src\projet-thermoregulation\arduino_thermocouple





class Terminal:
    def __init__(self, com_port, baud_rate=9600, timeout=0.0) -> None:
        self.connected = False
        self.prompt = "Arduino >> "
        self.encoding = 'utf-8'
        self.is_reader_alive = False
        self.reader = threading.Thread(target=self.receive_reply, name='rx')
        self.reader.daemon = True
        self.arduino = serial.Serial(com_port,
                                     baud_rate,
                                     timeout=timeout)



    def send_message(self):


        if os.path.isfile(write_to_file_path): # checks if the .txt file where you want to collect data is already created or not. If not you will have to enter the experiments parameters. 
            message = input(self.prompt).encode(self.encoding)

            if message == b'exit!': # enable you to shut down the communication with the chip at any time 
                self.connected = False
                self.is_reader_alive = False
                self.reader.join()

            self.arduino.write(message)
        
        else :     #if .txt file is empty, then it is the first message 
            print("\n Let's get started ! \n")
           
            message1 = input(self.prompt + "What is your time unit (in seconds) ? ")
            message2 = input(self.prompt + "How long should the measurements last (in time unit) ? ")
            message = message1 +","+ message2
            message = message.encode(self.encoding)
            
            print("\nProcessing...\n")  
        

            if message == b'exit!' :
                self.connected = False
                self.is_reader_alive = False
                self.reader.join()
            
            self.arduino.write(message)
         
            time.sleep(10) #delay needed to let the time to create the file after the first call of send_message, progress to be made 
            
            
    def receive_reply(self):
        while self.connected and self.is_reader_alive:
            reply = self.arduino.readline().decode(self.encoding)
            
            try:
                is_valid = ord(reply) != 32 and ord(reply) != 13
            except TypeError:
                is_valid = True

            
            if reply and is_valid:
                output_file = open(write_to_file_path, "a")  # opens the .txt file where you want to store your data
                output_file.write("\n" + str(time.time()) + "\n") # adds the absolute time in seconds when the data was taken
                output_file.write(reply) # adds the according data
                output_file.close()


            if reply == "The End." : # receives the end signal from the Arduino chip. It means that the total amount of time has elapsed 
                self.connected = False
                self.is_reader_alive = False
                print("Measurements are done. Press Enter to get your graph.") # until a better solution you will have to manually press enter to see your data plotted 

            time.sleep(2)
            


    def start_terminal(self):
        try:
            self.connected = True
            self.is_reader_alive = True
            self.reader.start()

            while self.connected:
                self.send_message()
                time.sleep(0.3)

        except Exception as e:
            print("[X] Exception :", e)


if __name__ == "__main__": 
    nameExp = input("Please enter the name of the experiment : ")
    write_to_file_path = "data/" + nameExp + ".txt" 
    serial_port = input("Please enter the name of the port : ") # in order to properly communicate with the Arduino chip you will have to manually enter the name of the port you are using to communicate with the chip. 
    ardterm = Terminal(serial_port)
    ardterm.start_terminal() # until the end signal coming from he Arduino chip indicating that the total amount time has elapsed, continues looking at the serial port to see if datat was sent, if so stores it



# initalising the needed arrays to plot our temperature measurments 
    time = arr.array('d', [])
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

        tempLine = tempLine.replace(" ", "")
        tempLine = tempLine.replace("\n", "")
        Temps = tempLine.split(",")
        for element in Temps : 
            if len(element) != 5 and len(element) != 4 :
                Temps.remove(element) # checks for corrupted data. Typically should look like an absent or partial temperature measurement that should normally look like '24.03'

        if len(Temps) == 4 : # if one temperature measurement is corrupted then the all set is deleted
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



