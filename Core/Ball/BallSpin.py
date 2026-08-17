"""
BallSpin.py
Quản lý độ xoáy của bóng
"""


class BallSpin:

    def __init__(self, ball):

        self.ball = ball

        self.spin_x = 0.0
        self.spin_y = 0.0
        self.spin_z = 0.0

    def set_spin(self, sx, sy, sz):

        self.spin_x = sx
        self.spin_y = sy
        self.spin_z = sz

    def clear(self):

        self.spin_x = 0
        self.spin_y = 0
        self.spin_z = 0

    def update(self):

        self.ball.velocity_x += self.spin_x * 0.01
        self.ball.velocity_y += self.spin_y * 0.01

        self.spin_x *= 0.99
        self.spin_y *= 0.99
        self.spin_z *= 0.99