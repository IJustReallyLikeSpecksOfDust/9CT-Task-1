#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random

#------------------------------------
ev3 = EV3Brick()

claw_motor = Motor(Port.D)


#------------------------------------
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()

def openClaw():
    claw_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=50)
    ev3.speaker.beep()





def closeClaw():
    claw_motor.run_until_stalled(-200,then=Stop.COAST, duty_limit=50)
    ev3.speaker.beep()