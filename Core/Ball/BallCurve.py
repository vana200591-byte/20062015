"""
BallCurve.py
Độ cong của bóng
"""


class BallCurve:

    def __init__(self, ball):

        self.ball = ball

        self.curve_strength = 0.0

    def set_curve(self, strength):

        self.curve_strength = strength

    def update(self):

        self.ball.velocity_x += self.curve_strength * 0.02

        self.curve_strength *= 0.97

    def clear(self):

        self.curve_strength = 0.0