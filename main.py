import pyfirmata
from pyfirmata import Arduino
import time


print('Test')



if __name__ == '__main__':
    board = Arduino('COM4') # establishing contact with the Arduino board via the choosen port 
    print("Communication Successfully started")
    
    for i in range(5):
        board.digital[13].write(1)
        time.sleep(10)
        print("LED set on")
        board.digital[13].write(0)
        time.sleep(1)
        