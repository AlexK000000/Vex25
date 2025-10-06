# vex 1155B Kestrel

import time
from vex import *


"""Global and Necessary Definitions"""

brain=Brain() #defines the brain variable, IMPORTANT: DO NOT REMOVE

ControllerType.PRIMARY #what is the difference between this and the next line, are both necesary? 
controller = Controller(PRIMARY)

myVariable = 0 #this is found nowhere else, can we delete
teamsidevariable = 1 #same here

"""Sensor Definitions"""

imu1 = Inertial(Ports.PORT13) 

"""Drivetrain Definitions"""

LeftD_F = Motor(Ports.PORT4,GearSetting.RATIO_18_1, True) #defines the motor variables, arguements are port, ratio, reverse?
LeftD_B = Motor(Ports.PORT3,GearSetting.RATIO_18_1, True)

RightD_F = Motor(Ports.PORT7,GearSetting.RATIO_18_1, False) 
RightD_B = Motor(Ports.PORT8,GearSetting.RATIO_18_1, False)

left_drive = MotorGroup(LeftD_F, LeftD_B,) #lets the left half of the DT move together
right_drive = MotorGroup(RightD_F, RightD_B) #lets the right half of the DT move together
drivetrain = DriveTrain(right_drive, left_drive) #lets the whole DT move together - use only when going straight - could we fit in the other arguements?
#what about the smartdrivetrain class?
"""Other Motor Definitions"""

intake = Motor(Ports.PORT10,GearSetting.RATIO_18_1, False) #should be replaced
Tchain = Motor(Ports.PORT6,GearSetting.RATIO_18_1, False)

#-------------------------------DRIVER PORTION OF THE CODE--------------------------------#

def driver(): # sets up the driver controls, namely pressing what buttons on the controller do on the robot
    """PLEASE DO NOT MESS WITH THESE 5 DEFINITIONS UNLESS THE VEXCODE EXTENSION CHANGES"""
    global r_pos 
    global l_pos
    global is_driver
    global mode 
    is_driver=True

    while True:
        right_drive.set_velocity(controller.axis2.position(), PERCENT) # makes the right drive move by what percentage forward the stick is
        right_drive.spin(FORWARD)

        left_drive.set_velocity(controller.axis3.position(), PERCENT) # makes the left drive move by what percentage forward the stick is
        left_drive.spin(FORWARD)

        if controller.buttonX.pressing(): # if button X is pressed then:
            Tchain.stop()

        if controller.buttonY.pressing(): # if button Y is pressed then:
            Tchain.set_velocity(100, PERCENT)
            Tchain.spin(FORWARD)
          
        if controller.buttonRight.pressing(): # if the right button is pressed then:
            Tchain.set_velocity(100, PERCENT)
            Tchain.spin(REVERSE) 


        if controller.buttonUp.pressing(): # if the up button is pressed then:
            intake.set_velocity(100, PERCENT)
            intake.spin(FORWARD)

        if controller.buttonDown.pressing(): # if the down button is pressed then:
            intake.stop()
        
        if controller.buttonLeft.pressing(): # if the left button is pressed then:
            intake.set_velocity(100, PERCENT)
            intake.spin(REVERSE)

    
#-----------------------------AUTONOMOUS PORTION OF THE CODE---------------------------------#

def autonomous(): # sets up the autonomous controls
    """PLEASE DO NOT MESS WITH THESE 4 DEFINITIONS UNLESS THE VEXCODE EXTENSION CHANGES"""
    global r_pos
    global l_pos
    global is_driver
    is_driver = False


competition = Competition(driver,autonomous)