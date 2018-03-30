#/usr/bin/python3

#University of Arizona Engineering Senior Design
# Team TANKS #17023
#Data point class for mesh network endpoint system
#Instantiate with data collected by the flow meter subsystems and conveniently
# package it in to JSON for use in a POST request

from time import localtime, strftime

class TANKSDataPoint:
    def __init__(self, radioID, flowRate):
        self.radioID = radioID
        self.flowRate = flowRate
        self.timestamp = strftime('%Y-%m-%dT%H:%M:%S.000Z',localtime())

    def toJSON(self):
        return('{"ID":"'+str(self.radioID)+'","time":"'+str(self.timestamp)+'","flowRate":"'+str(self.flowRate)+'"}')
