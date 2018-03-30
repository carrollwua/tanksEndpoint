#/usr/bin/python3

#University of Arizona Engineering Senior Design
# Team TANKS #17023
#Mesh network endpoint python for extracting data from the mesh network,
# packing it into a POST request, and sendint it to the server
#
#Upon startup, this will create a log file and keep a record of transactions

#import libraries

import serial
import TANKSDataPoint 
from time import localtime, strftime

#Globals and settings

serialDevice = '/dev/ttyACM0'
baudRate = 9600
logFilename = '/home/pi/TANKS/logs/' + strftime('%Y-%m-%d-%H-%M-%S', localtime()) + '.log'

ser = serial.Serial(serialDevice, baudRate)
logFile = open(logFilename, 'a+')

while True:
    serLine = ser.readline().decode().strip()
    logFile.write(serLine + '\n')
    lineParts = serLine.split(' ')
    if (lineParts[0] == 'FS') and (len(lineParts) >= 3):
        point = TANKSDataPoint.TANKSDataPoint(lineParts[2],lineParts[1])
        
        
