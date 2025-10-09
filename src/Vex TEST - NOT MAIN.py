# vex 1155B Kestrel

import time
from vex import *
import math

"""Global and Necessary Definitions"""

brain=Brain() #defines the brain variable, IMPORTANT: DO NOT REMOVE

ControllerType.PRIMARY #what is the difference between this and the next line, are both necesary? 
controller = Controller(PRIMARY)

myVariable = 0 #this is found nowhere else, can we delete
teamsidevariable = 1 #same here

"""Sensor Definitions"""

imu1 = Inertial(Ports.PORT13) 

"""Drivetrain Definitions"""

LeftD_F = Motor(Ports.PORT4,GearSetting.RATIO_18_1, False) #defines the motor variables, arguements are port, ratio, reverse?
LeftD_B = Motor(Ports.PORT3,GearSetting.RATIO_18_1, False)

RightD_F = Motor(Ports.PORT7,GearSetting.RATIO_18_1, True) 
RightD_B = Motor(Ports.PORT8,GearSetting.RATIO_18_1, True)

right_drive = MotorGroup(LeftD_F, LeftD_B,) #lets the left half of the DT move together
left_drive = MotorGroup(RightD_F, RightD_B) #lets the right half of the DT move together
drivetrain = SmartDrive(right_drive, left_drive, imu1,(3.25 * math.pi),13.95,13,INCHES) #lets the whole DT move together - use only when going straight - could we fit in the other arguements?
#what about the smartdrivetrain class?
"""Other Motor Definitions"""

intake = Motor(Ports.PORT10,GearSetting.RATIO_18_1, False) #should be replaced
Tchain = Motor(Ports.PORT6,GearSetting.RATIO_18_1, False)

#---------------------------------------------------------------#

def driver(): # sets up the driver controls, namely pressing what buttons on the controller do on the robot
    """PLEASE DO NOT MESS WITH THESE 5 DEFINITIONS UNLESS THE VEXCODE EXTENSION CHANGES"""
    global r_pos 
    global l_pos
    global is_driver
    global mode 
    is_driver=True
    
    while True:
        right_drive.set_velocity(controller.axis2.position(), PERCENT) #makes the right drive move by what percentage forward the stick is
        right_drive.spin(FORWARD)

        left_drive.set_velocity(controller.axis3.position(), PERCENT) #makes the left drive move by what percentage forward the stick is
        left_drive.spin(FORWARD)

        if controller.buttonX.pressing():
            Tchain.stop()

        if controller.buttonY.pressing():
            Tchain.set_velocity(100, PERCENT)
            Tchain.spin(FORWARD)
          
        if controller.buttonRight.pressing():
            drivetrain.drive_for(FORWARD, 10)
            drivetrain.turn_to_heading(90)
            drivetrain.drive_for(FORWARD, 10)
            drivetrain.turn_to_heading(90)
            drivetrain.drive_for(FORWARD, 10)
            drivetrain.turn_to_heading(90)
            drivetrain.drive_for(FORWARD, 10)
            drivetrain.turn_to_heading(90)
        
        if controller.buttonUp.pressing():
            intake.set_velocity(100, PERCENT)
            intake.spin(FORWARD)

        if controller.buttonDown.pressing():
            intake.stop()
        
        if controller.buttonLeft.pressing():
            drivetrain.drive_for(REVERSE, 10)

    
#---------------------------------------------------------------

def autonomous():
    global r_pos
    global l_pos
    global is_driver
    is_driver = False


competition = Competition(driver,autonomous)