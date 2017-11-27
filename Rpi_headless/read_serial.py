'''
Created on Nov 25, 2017

@author: TZ-WORKSTATION
'''
import serial

# this class read from serial 
arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)

def isActive():
    if arduinoSerialData !=0: return True
    else: return False
        

def printLive():
    while isActive:
        if(arduinoSerialData.inWaiting(),0):
            data = arduinoSerialData.readline()
            print (data)

def getData():
    return int(printLive())            