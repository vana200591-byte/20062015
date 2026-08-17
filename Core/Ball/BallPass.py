"""
BallPass.py
Thực hiện đường chuyền
"""


class BallPass:

    def __init__(self, ball):

        self.ball = ball

    def short_pass(self, player, target_x, target_y):

        self.ball.owner.clear()

        self.ball.last_touch = player

        self.ball.velocity_x = (target_x - self.ball.x) * 0.15

        self.ball.velocity_y = (target_y - self.ball.y) * 0.15

        self.ball.velocity_z = 0.05

    def long_pass(self, player, target_x, target_y):

        self.ball.owner.clear()

        self.ball.last_touch = player

        self.ball.velocity_x = (target_x - self.ball.x) * 0.10

        self.ball.velocity_y = (target_y - self.ball.y) * 0.10

        self.ball.velocity_z = 1.8