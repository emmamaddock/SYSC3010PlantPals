'''
Created on Dec 2, 2017

@author: Muhammad Tarequzzaman | 100954008
'''
import requests as R
import Read_serial as serial 
import json as Js
import json
serverIP = '192.168.0.14'
serverURL1='http://192.168.0.14/tarik2.php'

#Plant1=moisture1&Plant2=moisture2&Plant3=moisture3'


global arduinoJson
arduinoJson= serial.returnSerial()

def printURL():
    arduinoJson= serial.returnSerial()
    data = json.loads(arduinoJson)
    
    A = str(data['Plant1'])
    B = str(data['Plant2'])
    C = str(data['Plant3'])
    
    URL = serverURL1 +'?Plant1='+A +'&Plant2='+B+ '&Plant3='+C
    #print URL
    return URL
   

def requestJson():
    q = R.get(serverURL1)
    print q.content
    return int(q.content)
    
def sendJson():
    r = R.post(printURL(), arduinoJson)
    #print r
    print(r.status_code,r.reason)

def send_requst():
    sendJson()
    return requestJson()  
    
    

