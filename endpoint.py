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
import requests
from time import localtime, strftime

#Globals and settings

logging = True

serialDevice = '/dev/ttyACM0'
baudRate = 9600

logFilename = '/home/pi/TANKS/logs/' + strftime('%Y-%m-%d-%H-%M-%S', localtime()) + '.log'
#targetURL = 'https://srerwater.wixsite.com/tanks/_functions/postflow'
targetURL = 'https://srerwater.wixsite.com/tanks/_functions-dev/postflow'

ser = serial.Serial(serialDevice, baudRate)

if logging:
    logFile = open(logFilename, 'a+')

while True:
    serLine = ser.readline().decode().strip()
    print(serLine)
    if logging:
        logFile.write(serLine + '\n')
    lineParts = serLine.split(' ')
    if (lineParts[0] == 'FS') and (len(lineParts) >= 3):
        point = TANKSDataPoint.TANKSDataPoint(lineParts[2],lineParts[1])
        print(point.toJSON())
        preq = requests.post(targetURL, json = point.toDict())
        print(preq.text)
        print(preq.status_code)
        if logging:
            logFile.write(str(preq.status_code) + ': ' + preq.text)
            logFile.write('\n')
