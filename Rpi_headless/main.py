'''
Created on Nov 25, 2017

@author: Muhammad Tarequzzaman |100954008|
'''

import StepperMotor as st
import pump as pu
#import read_serial as rs
import RPi.GPIO as GPIO
import time
import SetupGPIO as set
import Send_Json_HTTP as SHTTP


set.setup_pump_GPIO(23)
set.setup_Stepper_GPIO()

SHTTP.requestJson()
SHTTP.sendJson()
#===============================================================================
# # give a value in Tf
# st.stepForward(200)
# st.stopMotor()
# #pu.deactivate()
# #time.sleep(5)
# pu.activate()
# time.sleep(5)
# pu.deactivate()
# 
# 
# time.sleep(1)
# st.stepBackward(200)
# st.stopMotor()
# pu.activate()
# time.sleep(1)
# pu.deactivate()
# 
# pu.cleanGPIO()
# st.cleanGPIO()
#===============================================================================


if __name__ == '__main__':
    pass
