'''
Created on Dec 2, 2017

@author: Caleb Gryfe |101009798| 
'''

import RPi.GPIO as GPIO
import time
import StepperMotor as st
import SetupGPIO as set
import pump as pu

GPIO.setmode(GPIO.BCM)
set.setup_Stepper_GPIO()
set.setup_pump_GPIO(23)

def plant1():
    st.stepForward(267)
    st.stopMotor()
    pu.activate()
    time.sleep(5)
    pu.deactivate()
    st.stepBackward(267)

def plant2():
    st.stepForward(533)
    pu.activate()
    pu.deactivate()
    st.stepBackward(533)

def plant3():
    st.stepForward(800)
    pu.activate()
    pu.deactivate()
    st.stepBackward(800)
    
    
    
