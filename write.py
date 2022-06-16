##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
import serial  # sudo pip install pyserial should work
import time

serial_port = 'COM3'
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "data/" + input("Nom du fichier .txt de données de températures : ") + ".txt"

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
#ser.close()
while True:
    line = ser.readline()
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    print(line)
    output_file.write("\n" + str(time.time()) + "\n")
    output_file.write(line)
    