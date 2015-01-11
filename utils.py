__author__ = 'Aidan O\'Brien'

import numpy as np


# Functions to ensure that the vectors created are in the correct format
def create_momentum_vector(i, j, k):
    return np.array([[i], [j], [k]])


def create_velocity_vector(i, j, k):
    return np.array([[i], [j], [k]])


def create_principles(i, j, k):
    return np.array([[i, 0, 0],
                     [0, j, 0],
                     [0, 0, k]])