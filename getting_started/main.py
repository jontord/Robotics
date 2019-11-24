#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
motor_a = Motor(Port.A)

brick.sound.beep()
wait(1000)
brick.sound.beep(800, 1000)
wait(1000)

motor_a.run_target(500, 720) #500 degrees per second, 90 target angle
brick.sound.beep(1000, 500) #frequency, duration



