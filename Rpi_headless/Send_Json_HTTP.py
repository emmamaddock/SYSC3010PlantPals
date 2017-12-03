'''
Created on Dec 2, 2017

@author: TZ-L
'''
import requests as R
import read_serial as serial 
import json
serverIP = '192.168.0.14'
serverURL = 'http://192.168.0.14/tarik.php?Plant1=8'
#jdata= serial.returnSerial()

jtest = {'Plant1':8}
jtest_json = json.dumps(jtest)

#data = {"temp_value":132}
#data_json = json.dumps(data)
payload = {'json_playload': jtest_json}


def requestJson():
     R.get(serverURL)
    
def sendJson():
    #R.get(serverURL, jtest_json = payload)
    #R.post(serverIP , jtest)
    r = R.post(serverURL, jtest_json)
    print(r.status_code,r.reason)
     

