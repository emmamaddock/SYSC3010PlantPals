'''
Created on Nov 26, 2017

@author: Muhammad Tarequzzaman |100954008|
'''
import RPi.GPIO as GPIO

def setupGPIO():
    ControlPin = [4,17,27,2,23]
    GPIO.setmode(GPIO.BCM)
    
# GPIO pin setting up  
    for pin in ControlPin:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    
  