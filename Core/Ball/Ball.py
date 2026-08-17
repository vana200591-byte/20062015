"""
Ball.py
Football Game v0.4
"""

from Ball.BallState import BallState
from Ball.BallOwner import BallOwner


class Ball:

    def __init__(self):

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.velocity_z = 0.0

        self.rotation = 0.0

        self.radius = 11

        self.weight = 0.43

        self.state = BallState()

        self.owner = BallOwner()

        self.last_touch = None

    def set_position(self, x, y):

        self.x = x
        self.y = y

    def set_height(self, z):

        self.z = z

    def update(self):

        self.x += self.velocity_x
        self.y += self.velocity_y
        self.z += self.velocity_z

    def stop(self):

        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity_z = 0

    def reset(self):

        self.x = 0
        self.y = 0
        self.z = 0

        self.stop()

    def get_position(self):

        return (self.x, self.y, self.z)