'''
Created on Nov 25, 2017

@author: TZ-WORKSTATION
'''

import StepperMotor as st
import pump as pu
import read_serial as rs
import RPi.GPIO as GPIO
import time
import SetupGPIO as set

set.setup_Stepper_GPIO()


# give a value in Tf
# st.stepForward(Tf)  

if __name__ == '__main__':
    pass