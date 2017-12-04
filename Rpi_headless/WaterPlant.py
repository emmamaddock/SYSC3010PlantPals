'''
Created on Dec 3, 2017

@author: Muhammad Tarequzzaman || 100954008
'''
import PlantSpecific as PS
import Http_server as hTTP
import Read_serial as sErial
import time

global getFromHttp 
#global postingToHttp
#= hTTP.sendJson()

def isConnection(): #boolean check for active serial connection
    if ((sErial.isActive() == True)  ):
        return True
def systemOprational():
#=======================================================================
#this is an automatic method to water the specific plant,
#it gets a http request from server to water a plant, which activate the predetermined position of watering         
#=======================================================================        
    while isConnection()==True:
        getFromHttp=hTTP.send_requst()
        print(getFromHttp)
        if (getFromHttp == 1):
            PS.plant1()
            print('Plant 1 has been watered ')
        elif(getFromHttp == 2):
            PS.plant2()
            print('Plant 2 has been watered ')
        elif(getFromHttp == 3):
            PS.plant3()
            print('Plant 3 has been watered ')
        else: 
            print('Do Nothing')
        time.sleep(5)
                        
            
            
    
        
        
        