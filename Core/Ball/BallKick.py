"""
BallKick.py
Thực hiện cú đá cơ bản
"""


class BallKick:

    def __init__(self, ball):

        self.ball = ball

    def kick(self, direction_x, direction_y, power):

        self.ball.owner.clear()

        self.ball.velocity_x = direction_x * power

        self.ball.velocity_y = direction_y * power

        self.ball.velocity_z = power * 0.15

        self.ball.last_touch = None

        print("Kick!")