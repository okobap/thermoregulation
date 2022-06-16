import serial
import time
import threading


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
       #message = input().encode(self.encoding)
        self.arduino.write(message)

        if message == b'exit!':
            self.connected = False
            self.is_reader_alive = False
            self.reader.join()


    def receive_reply(self):
        while self.connected and self.is_reader_alive:
            reply = self.arduino.readline().decode(self.encoding)
            try:
                is_valid = ord(reply) != 32 and ord(reply) != 13
            except TypeError:
                is_valid = True
            if reply and is_valid:
                #print(f"\nReply --> {reply}\n{self.prompt}", end='')
                print(reply)
                output_file = open(write_to_file_path, "a")
                output_file.write("\n" + str(time.time()) + "\n")
                output_file.write(reply)
                output_file.close()
            time.sleep(1)

            
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
    write_to_file_path = "data/" + input("Nom du fichier .txt de données de températures : ") + ".txt"
    serial_port = input("enter name of the port : ")
    #output_file = open(write_to_file_path, "w+")
    ardterm = Terminal(serial_port)
    ardterm.start_terminal()
    
    
    

