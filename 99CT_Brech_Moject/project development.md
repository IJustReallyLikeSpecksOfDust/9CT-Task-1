# Assessment Task One
### By Maxi Falconer-Ware


# Requirements Outline
## Purpose

I must develop a program that allows an EV3 Lego Mindstorms robot to find, transport, drop, and avoid, a set of coloured blocks.
The robot is required to use at least 2 different sensors, with all other attachments being removable after each lesson.

## Key Actions

##### Move - The robot needs to be able to drive, turn, and move in other basic ways.
##### Detect - The robot will need to detect obstacles and targets in front of it.
##### Acquire - The robot must be able to pick up/otherwise acquire the objects it must...
##### Transport - The robot must be able to transport objects it hold from place to place.

## Functional Requirements

The robot must drive straightforward in a path set by the code. It should also turn alongside that.

When the ultrasonic sensor detects an object in front of it, the robot should use it's colour sensor to detect if it is a target or something that must be evaded, and respond appropriately by either acquiring the object or turning and moving in a different direction.

Upon detecting an object it needs to acquire, the robot should pick it up or otherwise control it's location.

When able too, the robot should transport it's object to the location it started in, by carrying/pushing/otherwise moving it.


## Use Cases


### Example 1


##### Scenario: The robot is required to find an object.

##### Input: None

##### Action: The robot begins to drive forward.

##### Expected Outcome: The robot moves directly forward.



### Example 2


##### Scenario: The robot is moving to find something and it finds an obstacle.

##### Input: The ultrasonic sensor detects something infront of the robot and the colour sensor identifies it as an obstacle.

##### Action: Turn left or right 90 degrees and move forwards.

##### Expected Outcome: The robot moves a distance from the obstacle.


### Example 3


##### Scenario: The robot is moving to find something and it finds a target.

##### Input: The ultrasonic sensor detects something infront of the robot and the colour sensor identifies it as a target.

##### Action: The robot uses an attachment to pick up the target. It then starts to move again.

##### Expected Outcome: The robot picks up it's target then continues.


### Example 4


##### Scenario: The robot has picked up an object and must continue.

##### Input: Previous occurences (example 3)

##### Action: The robot turns backwards and moves until it reaches a boundary. Then, it navigates the boundary by sticking with the black path (using the colour sensor) until it reaches it's destination.

##### Expected Outcome: The robot transports it's target from it's original location to a different, specified location.



## Test Cases

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Must find object      |None           |Robot drives forward                 |
|        Encounters obstacle   | Ultrasonic Sensor detects object & colour sensor identifies it as obstacle   |   Robot turns 90 degrees and continues                |
|Encounters target   |Ultrasonic Sensor detects object & colour sensor identifies it as target           |    Robot uses attachment(s) to pick up the object and continues               |
|Reaches drop-off point         |  Colour sensor detects large black square area         |   Robot drops objects into the point and continues/succeeds                |



## Non-Functional Requirements


- Speed
The robot must move swiftly for ease of testing and general utility.

- Precison
The robot needs to be able to move precisely as to not accidentally bump objects or leave it's area.

- Reaction Time
The robot should react to sensor information swiftly.





# Design

### Identify and collect a block
```
BEGIN identify_obtain
	INPUT distance
	INPUT objectColour
	IF distance < 150 AND objectColour == yellow OR red
		openClaw
		drive forwards 50 millimetres
		closeClaw
	ENDIF
END identify_object
```

### Identify and evade a block.
```
BEGIN identify_evade
	INPUT distance
	INPUT objectColour
	IF distance < 150 AND objectColour == blue OR green
		Turn left 90 degrees
		IF distance < 150 AND objectColour == blue OR green
		Turn right 180 degrees
	ENDIF
END identify_evade
```

### Follow a line to the drop off and deposit a block.
```
BEGIN deposit
	followline
	openClaw
	IF priordeposits == 2
		Drive backwards 50 millimetres
		Turn left 90 degrees
	ELSEIF priordeposits == 1
		priordesposits = 2
	ENDIF
END deposit
```





# Development & Integration

#### Initial testing of claw function(s). Used for acquiring objects upon target encounter.

```
def openClaw(): 
    claw_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=50)
    ev3.speaker.beep()
```

There was a large amount of testing that went into the physical claw, that of course can't be reflected by code blocks.
One issue arose where the claw did not spin. I noticed that some pieces were, oddly, pushed out, and simply pushing
those back in fixed it.


#### Here is the entire first draft of the program.

```
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# may add more imports in the future.


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
driveSpeed = 100
PROPORTIONAL_GAIN = 1.2


def closeClaw():  #this has not yet been tested. It is a theory on how to make it work.
    claw_motor.run_until_stalled(-200,then=Stop.COAST, duty_limit=50) 
    ev3.speaker.beep()

def openClaw():  #has been tested and mostly works. may have an issue with it not "stalling". test different values for "duty_limit"
    claw_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=50)
    ev3.speaker.beep()

def followLine(): 
"""
code for making the robot follow the line.
Uses a lot of different values, with influence from colour sensor things.
driveSpeed and turn_rate are what decide the angle at which the robot turns whilst driving (does that make sense?).
"""
    ev3.speaker.beep()
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    while obstacle_sensor.distance() > 130:
        robot.drive(driveSpeed, turn_rate)
        wait(10)
    ev3.speaker.beep()


closeClaw() #to start at a default setting
followLine() #should go to top of circle
robot.turn(90) #need a way to make this work regardless of if it's coming from left or right
OpenClaw()
robot.drive(130)
closeClaw()
robot.drive(-130)
robot.turn(-90)  
followLine() #this function does not do what I want it too.
robot.turn(90)
openClaw() #deposit
robot.turn(90)  
followLine()
robot.turn(30)
closeClaw()
robot.turn(150)
followLine()
robot.turn(90)
openClaw() #deposit
#in theory this will work, otherwise
if obstacle_sensor.distance() > 100: #a different system for switching allisSwell would be a good idea. this is largely a placeholder (I hope) 
    allisSwell = 2

while allisSwell == 2: 
    """this loop acts as a failsafe, and should repeat until success occurs. It, quite simply, detects the distance of objects.
    If far, it will drive forwards, randomly decide if to turn or not, and continue.
    """
    while obstacle_sensor.distance() > 130:
        rng = random.randint(1,3)
        robot.drive(100)
        if rng == 2:
            robot.turn(90)
        elif rng == 3:
            robot.turn(-90)
        ev3.speaker.beep()
	if friendorfoe == 1:
	    openClaw()
	    robot.drive(50)
	    closeClaw()
	    robot.drive(-50)
	    robot.turn(90)
	elif friendorfoe == 2:
        rng = random.randint(1,2)
        robot.drive(100)
        if rng == 1:
            robot.turn(90)
        elif rng == 2:
            robot.turn(-90)

```
#### Major issues:
1.  closeClaw does not work.
2.  followLine does not do what I had hoped it would. Cannot be set to only follow for a specific time/length.
3.  I have no way to assign a value to friendorfoe. I need another colour sensor.
4.  Values need looots of testing, as expected.




# Testing and Debugging

## Test Case: Robot must find objects
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Must find object      |None           |Robot drives forward                 |

#### The robot needs to:
- Drive
- Turn

```
robot.drive(x)
robot.turn(x)
```

#### Test Evaluation:
- It performs the built in functions as expected.
- I used "x" for the arguments in the above code block to represent any number, as it varies.
- In hindsight, including this as a test case was pointless, as it is just a given for the robot. Due to this simplicity, no iteration is/was/will be required. Moving on.



## Test Case: Encounters Obstacle
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|        Encounters obstacle   | Ultrasonic Sensor detects object & colour sensor identifies it as obstacle   |   Robot turns 90 degrees and continues         

#### The robot needs to:

- Identify that an object is an obstacle
- Turn away in response

```
	elif friendorfoe == 2:
        rng = random.randint(1,2)
        robot.drive(100)
        if rng == 1:
            robot.turn(90)
        elif rng == 2:
            robot.turn(-90)

```
I don't currently have a way to detect an object's status. 
The actual evasion is quite simple. The only complexity is just randomness. 
As a placeholer/terrible replacement for detection, here is a version with another random. Recently put in main.py
```
	friendorfoe = random.randint(1,2)
	if friendorfoe == 1:
	#code for if the object is assumed to be a target
	elif friendorfoe == 2:
        rng = random.randint(1,2)
        robot.drive(100)
        if rng == 1:
            robot.turn(90)
        elif rng == 2:
            robot.turn(-90)
```

#### Test Evaluation:
- The robot's evasion is sufficient, although I haven't time to create a proper colour-detection function, and thus the placeholder remains.
- I used random as a method of making the turn function work, well, randomly.
- Evading was very easy. However, as has been made obvious, the detection is a massive sore point.
- I could certainly improve this by making a function that utilises a second colour-sensor, that would theoretically be facing forward, to detect the colour.

## Test Case: Encounters Target
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Encounters target   |Ultrasonic Sensor detects object & colour sensor identifies it as target           |    Robot uses attachment(s) to pick up the object and continues               |

The robot needs to:

- Identify that an object is a target
- Open the claw
- Approach
- Close the claw (trapping or gripping the object)
- Return

```
	if friendorfoe == 1:
		openClaw()
    	robot.drive(50)
    	closeClaw()
    	robot.drive(-50)
    	robot.turn(90)
```
This test case proves noticeably (too?) similar to Encounters Obstacle, and faces similar issues. Mainly the same lack of ability to detect a value for friendorfoe.
I already made an update for the prior test, so i'll just put that here too. Just gives randomness to friendorfoe.
```
	friendorfoe = random.randint(1,2)
	if friendorfoe == 1:
		openClaw()
    	robot.drive(50)
    	closeClaw()
    	robot.drive(-50)
    	robot.turn(90)
```

The real issues with this are the claw functions, which have a lot of problems. The versions used currently are:
```
def closeClaw():  
    claw_motor.run_until_stalled(-200,then=Stop.COAST, duty_limit=10)
    ev3.speaker.beep()
```
```
def openClaw():  
    claw_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=10)
    ev3.speaker.beep()
```
openClaw works, though the closeClaw above has not yet been tested (as of writing), and is among multiple other closeClaw tests.

#### Test Evaluation:
- Refer to the dot points for Test Case: Encounters Obstacle for referrence to detection, as the situation is virtually identical.
- As for the claw grabbing; yeah, it was a struggle. Too much testing time has been spent on it, quite troubling.
- It was, surprisngly, a surprise to me that this was so similar to Encounters Obstacle. I probably should've seen it coming, but it was good nonetheless.
- I just, begrudgingly, need more test time to make the claw function peak-ly. (that's not a word is it...) 





# Evaluation

### Individual Final Test - Functional
Well. At time of writing, the robot can obviously move, turn, beep, etc. All of those basic functions work well, although that is not an accomplishment--laugh out loud. The ultrasonic sensor usually works fine in tests, although values could be tinkered with for some functions/processes. The colour sensor (more specifically it's use in the following the line) seems to have a bug that came up in the group's final test, though it may be something else. The code for avoiding objects works, but the claw--and thus the collection weren't finished. So that was... Not great. 

### Individual Final Test - Non-Functional
Well. In terms of speed, the robot is fine. Basically default, honestly, but it works well enough. As for the precision factor, it absolutely shouldn't bump anything although with the use of randoness in the loop's turns, it could theoretically accidentally just walk outside the area. The reaction time is as seemless as can be, with sensor information used swiftly after it was gained. So like... could be worse?

### Group's Final Performance
It spun around for approximately ~8 seconds until it hit one of the obstacles. Self-explanatory. I think the group did fine, but this was unexpected and not planned for, to say the least... Oof. Wish I more to say here.

### Project Management
M.U.R.D.E.R Group was generally productive at all times throughout the project. We completed the research efficiently, and there was little to no wasted time. Though, it should be said that certain things that stunted progress, which caused us (or at least me) to fall behind given some time. I was terrible at pseudocode and flowcharts, which caused some time-waste before I decided to put it off. Additionally, we both used fairly elaborate additions, which necessitated a troublesome amount of building time, bug-fixing, and additional code. I believe our project management was quite far from perfect, and I will be attempting to remedy this in my future projects.

### Team Collaboration
Me and Benji were a fairly efficient team, or at least I think so. It would be kinda funny if in his evaluation he put "we were a mistake of a team" or something, but I should probably stick to the point. We bounced off each other with ideas quite well, were both quite efficient and didn't waste time. Working as a team was beneficial as I was able to get advice quite often, and it was cool to see another person's solution. Our collaboration wasn't hindered by being a duo, because larger groups do often lead to disorganisation or distraction. Overall, good collaboration methinks.

### Future Improvements that could be made - Justification
There is soooo much to improve. I'll start by stating the obvious. A function for detecting the colour of an object--specifically with another colour sensor--would assist the loop solution greatly, replacing the randomness. Also obviously, more testing for the claw functions, so that they work better, would be great. I had lots of ideas on fixing those. And of course, hardcoding that actually works would be great. It would've been rather time consuming, but far more consistent than what I have. So I really should've done some heavy editing to followLine, too. One more thing is the slant the physical claw ended up with is far from ideal, that warrants improvement, as It makes the claw a lot less precise.

## Some Final Thoughts - Not an Assessment Requirement
I am thoroughly dissatisfied with my failings in regards to (primarily) testing. Too much time was spent on the claw, which took far too much time to test, especially given the lower volume of rescources assisting me due to it being a more customised attachment. While it works theoretically as a method, I wasn't able to make it practical especially in comparison to the pushers I've seen used by other groups and my peer in M.U.R.D.E.R Group. Additionally, it was frustrating that our robot was out-of-commision for the crucial last two lessons of testing, especially when that was when I was making an attempt to hardcode. Also it took me far too long to realise that the usage of a second colour sensor would be required. That was not very bright. Hopefully my future projects attain more success.