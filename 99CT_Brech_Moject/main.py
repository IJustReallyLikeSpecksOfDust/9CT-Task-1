#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random


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
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2
DRIVE_SPEED = 100
PROPORTIONAL_GAIN = 1.2


def closeClaw():  
    claw_motor.run_until_stalled(-200,then=Stop.COAST, duty_limit=10)
    ev3.speaker.beep()

def openClaw():  
    '''A relatively simple, but crucial function that will likely require innovation.'''
    claw_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=10)
    ev3.speaker.beep()

def followLine(): #code for making the robot follow the line
    ev3.speaker.beep()
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 130:
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(10)
    ev3.speaker.beep()


 
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
#in theory this will work, otherwise
if obstacle_sensor.distance() > 100:
    allisSwell = 2

while allisSwell == 2: 
    """this loop acts as a failsafe, and should repeat until success occurs. It, quite simply, detects the distance of objects.
    If far, it will drive forwards, randomly decide if to turn or not, and continue.
    """
    while obstacle_sensor.distance() > 130:
        rng = random.randint(1,4)
        robot.drive(100)
        if rng == 3:
            robot.turn(90)
        elif rng == 4:
            robot.turn(-90)
        ev3.speaker.beep()
    openClaw()
    robot.drive(50)
    closeClaw()
    robot.drive(-50)
    robot.turn(90)

    