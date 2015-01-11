__author__ = 'Aidan O\'Brien'

import structure
import numpy as np
import numpy.linalg as linalg
import utils


# Calculates the effect the momentum wheels have upon the base structure
class Wheels():
    def __init__(self, wheel_x=np.zeros((3, 3)), wheel_y=np.zeros((3, 3)), wheel_z=np.zeros((3, 3))):
        if wheel_x.shape == (3, 3):
            self.wheel_x = wheel_x

        if wheel_y.shape == (3, 3):
            self.wheel_y = wheel_y

        if wheel_z.shape == (3, 3):
            self.wheel_z = wheel_z

        self.wheel_structure = np.zeros((3, 3))
        self.wheel_totals = np.zeros((3, 3))
        self.wheel_free = np.zeros((3, 3))

        self.calculate_wheel_structure(wheel_x=wheel_x, wheel_y=wheel_y, wheel_z=wheel_z)
        self.calculate_wheel_totals(wheel_x=wheel_x, wheel_y=wheel_y, wheel_z=wheel_z)
        self.calculate_wheel_free()

    def set_wheel_x(self, wheel_x=np.zeros((3, 3))):
        self.wheel_x = wheel_x

    def set_wheel_y(self, wheel_y=np.zeros((3, 3))):
        self.wheel_y = wheel_y

    def set_wheel_z(self, wheel_z=np.zeros((3, 3))):
        self.wheel_z = wheel_z

    # Calculating the moments of the wheel assembly that are fixed to the structure
    def calculate_wheel_structure(self, wheel_x=np.zeros((3, 3)), wheel_y=np.zeros((3, 3)), wheel_z=np.zeros((3, 3))):
        self.wheel_structure[0, 0] = wheel_y[0, 0] + wheel_z[0, 0]
        self.wheel_structure[1, 1] = wheel_x[1, 1] + wheel_z[1, 1]
        self.wheel_structure[2, 2] = wheel_x[2, 2] + wheel_y[2, 2]

    # Calculating the moments of the total wheel assembly
    def calculate_wheel_totals(self, wheel_x=np.zeros((3, 3)), wheel_y=np.zeros((3, 3)), wheel_z=np.zeros((3, 3))):
        self.wheel_totals = np.zeros((3, 3)) + wheel_x + wheel_y + wheel_z

    def calculate_wheel_free(self):
        self.wheel_free = self.wheel_totals - self.wheel_structure

    def calculate_required_wheel_speed(self, wheel_momentum=np.zeros((3, 1))):
        return linalg.solve(self.wheel_totals, wheel_momentum)