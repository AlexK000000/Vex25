# vex 1155B Kestrel

import time
from vex import *
import math

"""Global and Necessary Definitions"""

plusminus = 1
Ocycle=3

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

#intake = Motor(Ports.PORT17,GearSetting.RATIO_18_1, False) port relegated to descore
#intake.set_velocity(100, PERCENT)

Tchain = Motor(Ports.PORT19,GearSetting.RATIO_18_1, False)
Tchain.set_velocity(100, PERCENT)

Ramp = Motor(Ports.PORT13,GearSetting.RATIO_18_1, False)
Ramp.set_velocity(7,PERCENT)

Intake = Motor(Ports.PORT17,GearSetting.RATIO_18_1, False)
Intake.set_velocity(100,PERCENT)

topspin = MotorGroup(outtakeL, outtakeR)

def ramppressu(x):
    Ramp.spin_to_position(10, DEGREES)

def ramppressd(x):
    Ramp.spin_to_position(-10, DEGREES)

def TFor() :
    if not Tchain.direction()==FORWARD:  
        Tchain.spin(FORWARD)
    else:  
        Tchain.stop()

def TRev():
    if not Tchain.direction==REVERSE:
        Tchain.spin(REVERSE)
    else:
        Tchain.stop()

def InFor():
    if not Intake.direction==FORWARD:
        Intake.spin(FORWARD)
    else:
        Intake.stop()

def InRev():
    if not Intake.direction==REVERSE:
        Intake.spin(REVERSE)
    else:
        Intake.stop()

#AI definitions - I object but at this point in time I shall humor ryan, I will no longer touch the code. When he can explain it to me then we shall talk.

WHEEL_DIAMETER_IN = 4.0
WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER_IN * math.pi
TRACK_WIDTH_IN = 12.0

DRIVE_SPEED = 50
TURN_SPEED = 40
OUTTAKE_SPEED = 100


def drive_inches(distance):
    degrees = (distance / WHEEL_CIRCUMFERENCE) * 360

    LeftDF.spin_for(FORWARD, degrees, DEGREES, DRIVE_SPEED, PERCENT, False)
    LeftDB.spin_for(FORWARD, degrees, DEGREES, DRIVE_SPEED, PERCENT, False)

    RightDF.spin_for(FORWARD, degrees, DEGREES, DRIVE_SPEED, PERCENT, False)
    RightDB.spin_for(FORWARD, degrees, DEGREES, DRIVE_SPEED, PERCENT, True)

def turn_left(deg):
    turn_circ = math.pi * TRACK_WIDTH_IN
    wheel_dist = (deg / 360) * turn_circ
    motor_deg = (wheel_dist / WHEEL_CIRCUMFERENCE) * 360

    LeftDF.spin_for(REVERSE, motor_deg, DEGREES, TURN_SPEED, PERCENT, False)
    LeftDB.spin_for(REVERSE, motor_deg, DEGREES, TURN_SPEED, PERCENT, False)

    RightDF.spin_for(FORWARD, motor_deg, DEGREES, TURN_SPEED, PERCENT, False)
    RightDB.spin_for(FORWARD, motor_deg, DEGREES, TURN_SPEED, PERCENT, True)



#---------------------------------------------------------------#

def driver(): # sets up the driver controls, namely pressing what buttons on the controller do on the robot
    """PLEASE DO NOT MESS WITH THESE 5 DEFINITIONS UNLESS THE VEXCODE EXTENSION CHANGES"""
    global r_pos 
    global l_pos
    global is_driver
    global mode 
    is_driver=True

    controller.buttonX.pressed(TFor)
    controller.buttonB.pressed(TRev)

    controller.buttonUp.pressed(InFor)
    controller.buttonDown.pressed(InRev)

    while True:
        right_drive.set_velocity(controller.axis2.position(), PERCENT) #makes the right drive move by what percentage forward the stick is
        right_drive.spin(FORWARD)

        left_drive.set_velocity(controller.axis3.position(), PERCENT) #makes the left drive move by what percentage forward the stick is
        left_drive.spin(FORWARD) 
        """
        if controller.buttonDown.pressing():
            deScore.spin(REVERSE)
        elif controller.buttonUp.pressing():
            deScore.spin(FORWARD)
        else:
            deScore.stop   """         
        
       # if controller.buttonRight.pressing():
        #    intake.stop()

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

    #Here begins AI code, once again I object, I shall not touch the code until Ryan can explain to me what it is that this does and the cost behind his making it.
    # 1. Drive backwards 36 inches
    drive_inches(-36)

    # 2. Turn left 45 degrees
    turn_left(43)

    # 3. Drive backwards 8 inches
    drive_inches(-8.5)

    # 4. START OUTTAKE (BACKWARDS) AFTER MOVEMENT
    outtakeL.spin(REVERSE, OUTTAKE_SPEED, PERCENT)
    outtakeR.spin(REVERSE, OUTTAKE_SPEED, PERCENT)

    """ bad human code
    drivetrain.drive_for(1,SECONDS)"""

competition = Competition(driver,autonomous)
