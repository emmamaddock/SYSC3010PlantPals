'''
Created on Nov 24, 2017

@author: Muhammad Tarequzzaman |100954008|
'''

import RPi.GPIO as GPIO
import time
# GPIO pin mode setting up 
GPIO.setmode(GPIO.BCM)

ControlPin = [4,17,27,22]
# GPIO pin setting up  
for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
    

# 'seq' is the full sequence of the step motor
seq = [   
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
    ]
# "fstep" is the forward sequence  of the stepper motor
fstep = [ 
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1]
    ]

# "fbackstep" is the backward sequence  of the stepper motor
fbackstep = [
    [1,0,0,1],
    [0,0,1,1],
    [0,1,1,0],
    [1,1,0,0]        
    ]    


    
def stepForward(Tf): # call this function to run stepper motor forward for given time in second as a argument.
    
    while Tf !=0:
        for halfstep in range(4):
            for pin in range(4):
                GPIO.output(ControlPin[pin], fstep[halfstep][pin])
                time.sleep(0.001)
        Tf=Tf-1

def stepBackward(Tb):  # call this function to run stepper motor backward for given time in second as a argument.
    
    while Tb !=0:
        for halfstep in range(4):
            for pin in range(4):
                GPIO.output(ControlPin[pin], fbackstep[halfstep][pin])
                time.sleep(0.001)	    
        Tb = Tb-1    
                    
    
    
def cleanGPIO(): # call this function to clean up GPIO setup 
    GPIO.cleanup()       
    
    