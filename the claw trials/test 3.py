#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
obstacle_sensor = UltrasonicSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
line_sensor = ColorSensor(Port.S3)
claw_motor = Motor(Port.D)


#possible claw method 3

def closeClaw():  
    claw_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=10)
    ev3.speaker.beep()
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)

#essentially just test 2 again but with "duty_limit" modified as it may be stopping test 2 from working

closeClaw()