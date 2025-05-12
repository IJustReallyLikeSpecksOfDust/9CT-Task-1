#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
obstacle_sensor = UltrasonicSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
line_sensor = ColorSensor(Port.S3)
claw_motor = Motor(Port.D)




def followLine(): #code for making the robot follow the line
    ev3.speaker.beep()
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 130:
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    ev3.speaker.beep()

def turn(): #code for making the robot turn and then move
    ev3.speaker.beep()
    robot.turn(90)
    ev3.speaker.beep()
    robot.straight(435)
    ev3.speaker.beep()
    robot.turn(90)
    ev3.speaker.beep()

def openClaw(): #code for opening the claw.
    claw_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=50)
    ev3.speaker.beep()
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)
    
def closeClaw():  #code for closing the claw, ideally trapping a block inside.
    claw_motor.run_until_stalled(-200,then=Stop.COAST, duty_limit=50)
    ev3.speaker.beep()

def errorTest():
if 

# Write your program here.
ev3.speaker.beep()
ev3.speaker.beep()

allisSwell = 1 #this determines the mode that the program takes. either planned course or trial and
funnyvariablename =

#actual process
 
closeClaw() #set it to a default at the beginning of the code
if allisSwell == 1:

    followLine() #make this go to red
    robot.turn(90)
    openClaw()
    robot.straight(150) #value can be changed as needed
    closeClaw()
    robot.turn(90)
    followLine() #make this one go to start
    robot.turn(90)
    openClaw() #deposit)
    robot.turn(90)  
    followLine() #to the yellow
    robot.turn(30)
    closeClaw()
    robot.turn(150)
    followLine() #make this one go to start
    robot.turn(90)
    openClaw() #deposit)
    #in theory this will work

while allisSwell == 2:
    