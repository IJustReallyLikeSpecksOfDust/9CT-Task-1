from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


#SETUPs
claw_motor = motor(Port.D)

#the functions

#make a motor rotate, moving gears which open the claw. ensure all pieces are FIRMLY pushed in or else this will not work.
def openclaw():
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    gripper_motor.run_target(200, -90)

#ditto except it's the opposite. may have some redundant code right now.
def closeclaw():
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    gripper_motor.run_target(200, 90)