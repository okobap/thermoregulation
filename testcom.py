from tkinter.messagebox import YES
import serial
import time
import threading
from time import process_time, sleep


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
        message = input(self.prompt).encode(self.encoding)
        self.arduino.write(message)

        if message == b'exit!':
            self.connected = False
            self.is_reader_alive = False
            self.reader.join()


    def receive_reply(self):
        while self.connected and self.is_reader_alive:
            reply = self.arduino.readline().decode(self.encoding)
            
            time.sleep(0.8)
            try:
                is_valid = ord(reply) != 32 and ord(reply) != 13
            except TypeError:
                is_valid = True
            if reply and is_valid:
                #print(f"\nReply --> {reply}\n{self.prompt}", end='')
                print(reply)
                output_file.write(reply)
                output_file.write("\n" + str(time.time()) + "\n")
            

                
             

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
    if input("Lancer la manip ?") == "yes" : 
        write_to_file_path = "data/" + input("Nom du fichier .txt de données de températures : ") + ".txt"
        serial_port = input("enter the name of the port : ") 
        output_file = open(write_to_file_path, "w+")
        output_file.flush()

        ardterm = Terminal(serial_port)
        ardterm.start_terminal()
        output_file.close()


        
      



