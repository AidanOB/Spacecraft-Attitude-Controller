__author__ = 'Aidan O\'Brien'

# Importing all the different forms of attitude control systems
import wheels

# The following are not implemented yet
import gyros
import thrusters
import magnetor


# Initial class prototype, to be completed later
class Controller(wheels.Wheels, gyros.Gyros, thrusters.Thrusters, magnetor.Magnetor):
    def __init__(self):
        pass