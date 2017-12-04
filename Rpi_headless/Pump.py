'''
Created on Nov 24, 2017

@author: Muhammad Tarequzzaman |100954008| 
'''
import RPi.GPIO as GPIO
#import time
import SetupGPIO as s
#setup pin
pin = s.pin


def activate():# Call this function to activate Water pump
        GPIO.output(pin,1) 
    
def deactivate():# Call this function to deactivate Water pump
    GPIO.output(pin,0)
     
def cleanGPIO():#Call this function to clean up GPIO 
    GPIO.cleanup()       