import serial
import time
import threading
import math
import os
import os.path

class Terminal:
    def __init__(self, com_port, path, baud_rate=9600, timeout=0.0, ) -> None:
        self.connected = False
        self.prompt = "Arduino >> "
        self.encoding = 'utf-8'
        self.is_reader_alive = False
        self.reader = threading.Thread(target=self.receive_reply, name='rx')
        self.reader.daemon = True
        self.write_to_file_path = path
        self.arduino = serial.Serial(com_port,
                                     baud_rate,
                                     timeout=timeout)



    def send_message(self):

        if len(open(self.write_to_file_path, "r").readlines()) != 0 : # checks if the .txt file where you want to collect data is already created or not. If not you will have to enter the experiments parameters. 
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
            
            time.sleep(5)
            
            
    def receive_reply(self):
        while self.connected and self.is_reader_alive:
            reply = self.arduino.readline().decode(self.encoding)
            #print(reply)
            
            try:
                is_valid = ord(reply) != 32 and ord(reply) != 13
            except TypeError:
                is_valid = True

            
            if reply and is_valid:
              #  print('I am valid')
                output_file = open(self.write_to_file_path, "a")  # opens the .txt file where you want to store your data
                output_file.write("\n" + str(time.time()) + "\n") # adds the absolute time in seconds when the data was taken
                output_file.write(reply) # adds the according data
                output_file.close()
 

            if reply[-8:] == "The End." : # receives the end signal from the Arduino chip. It means that the total amount of time has elapsed 
               # print('I also am the End!')
                self.connected = False
                self.is_reader_alive = False
                print("Measurements are done. Press Enter to get your graph.") # until a better solution you will have to manually press enter to see your data plotted 

            time.sleep(0.2)
            


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