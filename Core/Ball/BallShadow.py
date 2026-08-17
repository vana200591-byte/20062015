"""
BallShadow.py
Bóng đổ của quả bóng
"""


class BallShadow:

    def __init__(self, ball):

        self.ball = ball

        self.scale = 1.0

    def update(self):

        height = self.ball.z

        self.scale = max(0.30, 1.0 - height * 0.05)

    def get_scale(self):

        return self.scale