__author__ = 'Aidan O\'Brien'

# External module imports
import numpy as np
import numpy.linalg as linalg

# Importing all the different forms of attitude control systems
import structure
import wheels


# The following are not implemented yet
import gyros
import thrusters
import magnetor


# Initial class prototype, to be completed later
class Controller(wheels.Wheels, gyros.Gyros, thrusters.Thrusters, magnetor.Magnetor, structure.Structure):
    def __init__(self,
                 structure_inertia=np.zeros((3, 3)), initial_angular_velocity=np.array([[0], [0], [0]]),
                 wheel_x=np.zeros((3, 3)), wheel_y=np.zeros((3, 3)), wheel_z=np.zeros((3, 3)),
                 mag_structure=np.zeros((3, 3)),
                 initial_momentum=np.zeros((3, 1))):

        wheels.Wheels.__init__(self, wheel_x=wheel_x, wheel_y=wheel_y, wheel_z=wheel_z)
        structure.Structure.__init__(self, structure_inertia=structure_inertia,
                                     initial_angular_velocity=initial_angular_velocity)
        magnetor.Magnetor.__init__(self, mag_structure=mag_structure)

        # Making correctly sized arrays initialised at zero
        # This ensures that the un-calculated elements are correct
        self.fixed_structure = np.zeros((3, 3))
        self.total_structure = np.zeros((3, 3))
        self.structure_momentum = np.zeros((3, 1))
        self.final_velocity = np.zeros((3, 1))
        self.delta_velocity = np.zeros((3, 1))
        self.final_momentum = np.zeros((3, 3))
        self.final_wheel_velocity = np.zeros((3, 1))

        self.combine_structure()

        self.calculate_structure_momentum()
        self.calculate_total_structure()
        self.calculate_current_momentum()

    def combine_structure(self):
        self.fixed_structure = self.structure_inertia + self.wheel_structure

    def calculate_total_structure(self):
        self.total_structure = self.structure_inertia + self.wheel_totals + self.mag_structure

    def calculate_structure_momentum(self):
        self.structure_momentum = self.fixed_structure.dot(self.angular_velocity)

    def calculate_current_momentum(self):
        self.momentum = self.total_structure.dot(self.angular_velocity)

    # Utilised when the change in momentum is known
    def calculate_final_velocity(self):
        self.final_velocity = linalg.solve(self.fixed_structure, (self.momentum + self.momentum_delta))

    def calculate_final_momentum(self):
        self.final_momentum = self.fixed_structure.dot(self.final_velocity)

    def set_final_velocity(self, final_velocity=np.zeros((3, 1))):
        self.final_velocity = final_velocity
        self.calculate_final_momentum()

    def calculate_final_conditions(self):
        self.final_wheel_velocity = self.calculate_required_wheel_speed(self.momentum - self.final_momentum)