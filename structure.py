__author__ = 'Aidan O\'Brien'

import numpy as np
import utils


class Structure:
    def __init__(self, structure_inertia=np.zeros((3, 3)), initial_angular_velocity=np.zeros((3, 1)),
                 initial_momentum=utils.create_momentum_vector(0, 0, 0)):
        self.structure_inertia = structure_inertia
        self.angular_velocity = initial_angular_velocity
        self.momentum = initial_momentum
        self.momentum_delta = np.array([[0], [0], [0]])

    def set_angular_velocity(self, i, j, k):
        self.angular_velocity = utils.create_velocity_vector(i, j, k)

    def set_structure_moments(self, a, b, c):
        self.structure_inertia = np.array([[a, 0, 0],
                                           [0, b, 0],
                                           [0, 0, c]])

    def set_current_momentum(self, i, j, k):
        self.momentum = np.array([[i], [j], [k]])

    # This function is for the case where the spacecraft is represented in a way that isn't around the principle axes
    def set_nonprinciple_moments(self, a1, a2, a3, b1, b2, b3, c1, c2, c3):
        self.structure_inertia = np.array([[a1, b1, c1],
                                           [a2, b2, c2],
                                           [a3, b3, c3]])

    def set_momentum_delta(self, delta_momentum=np.zeros((3, 1))):
        self.momentum_delta = delta_momentum