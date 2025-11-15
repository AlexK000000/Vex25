# vex 1155B Kestrel

import time
from vex import *
import math

"""Global and Necessary Definitions"""

plusminus = 1

brain=Brain() #defines the brain variable, IMPORTANT: DO NOT REMOVE

ControllerType.PRIMARY #what is the difference between this and the next line, are both necesary? 
controller = Controller(PRIMARY)

myVariable = 0 #this is found nowhere else, can we delete
teamsidevariable = 1 #same here

"""Sensor Definitions"""

imu1 = Inertial(Ports.PORT21) 

"""Drivetrain Definitions"""

RightDF = Motor(Ports.PORT15,GearSetting.RATIO_18_1, False) #defines the motor variables, arguements are port, ratio, reverse?
RightDB = Motor(Ports.PORT14,GearSetting.RATIO_18_1, False)
RightDF.set_velocity(100, PERCENT)
RightDB.set_velocity(100, PERCENT)

LeftDF = Motor(Ports.PORT10,GearSetting.RATIO_18_1, True) 
LeftDB = Motor(Ports.PORT11,GearSetting.RATIO_18_1, True)
LeftDF.set_velocity(100, PERCENT)
LeftDB.set_velocity(100, PERCENT)


outtakeR = Motor(Ports.PORT16,GearSetting.RATIO_18_1, True)
outtakeL = Motor(Ports.PORT18,GearSetting.RATIO_18_1, False)
outtakeL.set_velocity(100, PERCENT)
outtakeR.set_velocity(100, PERCENT)


right_drive = MotorGroup(RightDF, RightDB,) #lets the left half of the DT move together
left_drive = MotorGroup(LeftDF, LeftDB) #lets the right half of the DT move together
drivetrain = SmartDrive(right_drive, left_drive, imu1,(3.25 * math.pi),13.95,13,INCHES) #lets the whole DT move together - use only when going straight - could we fit in the other arguements?
#what about the smartdrivetrain class?
"""Other Motor Definitions"""

intake = Motor(Ports.PORT17,GearSetting.RATIO_18_1, False) 
intake.set_velocity(100, PERCENT)

Tchain = Motor(Ports.PORT19,GearSetting.RATIO_18_1, False)
Tchain.set_velocity(100, PERCENT)

Ramp = Motor(Ports.PORT13,GearSetting.RATIO_18_1, False)
Ramp.set_velocity(7,PERCENT)

topspin = MotorGroup(outtakeL, outtakeR)

#---------------------------------------------------------------#

def driver(): # sets up the driver controls, namely pressing what buttons on the controller do on the robot
    """PLEASE DO NOT MESS WITH THESE 5 DEFINITIONS UNLESS THE VEXCODE EXTENSION CHANGES"""
    global r_pos 
    global l_pos
    global is_driver
    global mode 
    is_driver=True


    while True:

        left_drive.set_velocity((controller.axis3.position()*(-(controller.axis1.position()))), PERCENT) #makes the left drive move by what percentage forward the stick is
        left_drive.spin(FORWARD)

        right_drive.set_velocity((controller.axis3.position()*controller.axis1.position()), PERCENT) #makes the left drive move by what percentage forward the stick is
        right_drive.spin(FORWARD)

        if controller.buttonX.pressing():
            Tchain.spin(REVERSE)

        if controller.buttonB.pressing():
            Tchain.spin(FORWARD)
          
        if controller.buttonY.pressing():
            Tchain.stop()
        
        if controller.buttonUp.pressing():
           intake.spin(FORWARD)

        if controller.buttonDown.pressing():
            intake.spin(REVERSE)
        
        if controller.buttonRight.pressing():
            intake.stop()

        if controller.buttonR2.pressing():
            topspin.spin(FORWARD)
        
        if controller.buttonL2.pressing():
            topspin.spin(REVERSE)
        
        if controller.buttonA.pressing():
            topspin.stop()
        
        if controller.buttonL1.pressing():
            Ramp.spin(FORWARD)
        elif controller.buttonR1.pressing():
            Ramp.spin(REVERSE)
        else:
            Ramp.stop()
        
        
        
        

    
#---------------------------------------------------------------

def autonomous():
    global r_pos
    global l_pos
    global is_driver
    is_driver = False

competition = Competition(driver,autonomous)
