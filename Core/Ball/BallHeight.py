"""
BallHeight.py
Quản lý độ cao của bóng
"""


class BallHeight:

    def __init__(self, ball):

        self.ball = ball

        self.max_height = 15.0

    def set_height(self, height):

        if height < 0:

            height = 0

        if height > self.max_height:

            height = self.max_height

        self.ball.z = height

    def get_height(self):

        return self.ball.z

    def is_grounded(self):

        return self.ball.z <= 0.0