'''
Created on Dec 2, 2017

@author: TZ-L
'''
import requests as R
import read_serial as serial 

serverIP = '192.168.0.14'
serverURL = 'http://192.168.0.14/tarik.php'
#jdata= serial.returnSerial()
jdata = '{"json":"TEST"}'

def requestJson():
    R.get(serverURL)
    
def sendJson():
     R.post(serverIP , jdata)
