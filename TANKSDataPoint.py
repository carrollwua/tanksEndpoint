#/usr/bin/python3

#University of Arizona Engineering Senior Design
# Team TANKS #17023
#Data point class for mesh network endpoint system
#Instantiate with data collected by the flow meter subsystems and conveniently
# package it in to JSON for use in a POST request

from time import localtime, strftime
import json

class TANKSDataPoint:
    def __init__(self, radioID, flowRate):
        self.radioID = radioID
        self.flowRate = flowRate
        self.timestamp = strftime('%Y-%m-%dT%H:%M:%S.000-0700',localtime())

    def toJSON(self):
        jsonString = '{"title":"' + str(self.radioID) + ' ' + self.timestamp + '", "node":' + self.radioID + ',"timeRecorded":' + self.timestamp + ',"averageFlow":' + self.flowRate + '}'
        print(jsonString)
        return json.dumps(jsonString) 
#        return json.dumps(self.toDict())
    
    def toDict(self):
        return {'title': (str(self.radioID) + '_' + self.timestamp), 'node':self.radioID,'timeRecorded':self.timestamp,'averageFlow':self.flowRate}
