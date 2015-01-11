__author__ = 'Aidan O\'Brien'

import structure
import numpy as np


# Initial empty class for filling inheritance purposes
class Magnetor():
    def __init__(self, mag_structure=np.zeros((3, 3))):
        self.mag_structure = mag_structure
