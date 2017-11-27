'''
Created on Nov 25, 2017

@author: TZ-WORKSTATION
'''

import StepperMotor as st
import pump as pu
import read_serial as rs
import RPi.GPIO as GPIO
import time

ControlPin = [4,17,27,22]
# GPIO pin setting up  
for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
    
pin = 23
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,0)

# give a value in Tf
# st.stepForward(Tf)  

if __name__ == '__main__':
    pass