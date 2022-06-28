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

if __name__ == "__main__": 
    nameExp = input("Please enter the name of the experiment : ")
    write_to_file_path = "data/" + nameExp + ".txt" 
    serial_port = input("Please enter the name of the port : ") # in order to properly communicate with the Arduino chip you will have to manually enter the name of the port you are using to communicate with the chip. 
    ardterm = Terminal(serial_port, write_to_file_path)
    ardterm.start_terminal() # until the end signal coming from he Arduino chip indicating that the total amount time has elapsed, continues looking at the serial port to see if datat was sent, if so stores it

    plotingAndSaving(nameExp, write_to_file_path)