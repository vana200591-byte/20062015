"""
BallReset.py
Đặt lại trạng thái bóng
"""


class BallReset:

    def __init__(self, ball):

        self.ball = ball

    def center(self):

        self.ball.x = 0.0
        self.ball.y = 0.0
        self.ball.z = 0.0

        self.ball.velocity_x = 0.0
        self.ball.velocity_y = 0.0
        self.ball.velocity_z = 0.0

        self.ball.owner.clear()

        self.ball.state.reset()

        self.ball.last_touch = None

    def goal_kick(self):

        self.center()

    def corner_kick(self):

        self.center()

    def throw_in(self):

        self.center()