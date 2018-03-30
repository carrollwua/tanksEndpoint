#/usr/bin/python3

import serial
from time import localtime, strftime

serialDevice = "/dev/ttyACM0"
baudRate = 9600
logFilename = "/home/pi/TANKS/logs/" + strftime("%Y-%m-%d-%H-%M-%S", localtime()) + ".log"


ser = serial.Serial(serialDevice, baudRate)
logFile = open(logFilename, 'a')

while True:
    serLine = ser.readline().decode().strip()
    
