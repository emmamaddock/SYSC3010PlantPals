'''
Created on Nov 26, 2017

@author: Muhammad Tarequzzaman |100954008|
'''
import RPi.GPIO as GPIO

#setting up GPIO pin for stepper motor
def setup_Stepper_GPIO():
    ControlPin = [4,17,27,22]
    GPIO.setmode(GPIO.BCM)   
# GPIO pin setting up  
    for pin in ControlPin:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)

#setting up Pump GPIO
def setup_pump_GPIO(pin):
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0) 
                
def cleanGPIO():#Call this function to clean up GPIO 
    GPIO.cleanup()             
