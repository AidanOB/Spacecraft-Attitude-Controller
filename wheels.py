__author__ = 'Aidan O\'Brien'

import structure
import numpy as np
import utils


# Calculates the effect the momentum wheels have upon the base structure
class Wheels(structure.Structure):
    def __init__(self, wheel_x, wheel_y, wheel_z):
        if wheel_x.shape == (3, 3):
            self.wheel_x = wheel_x
        else:
            self.wheel_x = np.zeros((3, 3))

        if wheel_y.shape == (3, 3):
            self.wheel_y = wheel_y
        else:
            self.wheel_y = np.zeros((3, 3))

        if wheel_z.shape == (3, 3):
            self.wheel_z = wheel_z
        else:
            self.wheel_z = np.zeros((3, 3))