'''
Created on Nov 26, 2017

@author: Muhammad Tarequzzaman |100954008|
'''
import RPi.GPIO as GPIO

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    ControlPin = [4,17,27,22]
# GPIO pin setting up  
    for pin in ControlPin:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    
    pin = 23
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,0)