# Assessment Task One
### By Maxi Falconer-Ware

## Purpose

I must develop a program that allows an EV3 Lego Mindstorms robot to find, transport, drop, and avoid, a set of coloured blocks.
The robot is required to us at least 2 different sensors, with all other attachments being removable after each lesson.

## Key Actions

##### Move - The robot needs to be able to drive, turn, and move in other basic ways.
##### Detect - The robot will need to detect obstacles and targets in front of it.
##### Acquire - The robot must be able to pick up/otherwise acquire the objects it must...
##### Transport - The robot must be able to transport objects it hold from place to place.

## Functional Requirements

The robot must drive straightforward in a path set by the code. It should also turn alongside that.

When the ultrasonic sensor detects an object in front of it, the robot should use it's colour sensor to detect if it is a target or something that must be evaded, and respond appropriately by either acquiring the object or turning and moving in a different direction.

Upon detecting an object it needs to acquire, the robot should pick it up or otherwise control it's location.

When able too, the robot should transport it's object to the location it started in, by carrying/pushing/etc-ing it.


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

- "The robot is stupid"