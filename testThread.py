import serial
import time
import threading

import matplotlib.pyplot as plt
import numpy as np
import array as arr
import math
import os
import os.path


from terminal import Terminal

from dataFinalPlot import *

from dataLivePlot import *




#This is to be used in order to launch an Temperature monitoring experiment. The total duration and period between temperature measurements are to be set via the terminal while the code is running. 
#You will also have to enter the 'name' of the port your are using to communicate with the Arduino chip on which the thermocouples are installed. This name should typically look like 'COM3'.

#After having collected all the data you will be invited to press enter, then the data will be ploted and the according figure saved with the .text data file

#At any time you should be able to shut down the communication with the Arduino chip by entering 'exit!' in the terminal when 'Arduino>>' is showing. 

#Be aware that when you shut down the communication with the Arduino chip, the code on the chip is still running. To completely shut down the chip and until a better solution you will have to unplug the alimentation of the chip

#The following script should be dowloaded to the Arduino chip in advance C:\Users\BaptisteVauleon\src\projet-thermoregulation\arduino_thermocouple


def listen_to_Arduino(ardterm):
     ardterm.start_terminal() # until the end signal coming from he Arduino chip indicating that the total amount time has elapsed, continues looking at the serial port to see if datat was sent, if so stores it

     #plotingAndSaving(nameExp, write_to_file_path)
     

if __name__ == "__main__": 
    nameExp = input("Please enter the name of the experiment : ")
    write_to_file_path = "data/" + nameExp + ".txt" 
    serial_port = input("Please enter the name of the port : ") # in order to properly communicate with the Arduino chip you will have to manually enter the name of the port you are using to communicate with the chip. 
    ardterm = Terminal(serial_port, write_to_file_path)


    number_of_lines_in_Tempfile = 0


    listen = threading.Thread(target=listen_to_Arduino, args=(ardterm,))
   
    listen.start()

    livePloting(nameExp, write_to_file_path, number_of_lines_in_Tempfile)

    listen.join()

    plotingAndSaving(nameExp, write_to_file_path)


    
    