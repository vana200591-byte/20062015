"""
BallShoot.py
Thực hiện cú sút
"""


class BallShoot:

    def __init__(self, ball):

        self.ball = ball

    def normal_shot(self, player, direction_x, direction_y):

        self.ball.owner.clear()

        self.ball.last_touch = player

        self.ball.velocity_x = direction_x * 18

        self.ball.velocity_y = direction_y * 18

        self.ball.velocity_z = 2.2

    def power_shot(self, player, direction_x, direction_y):

        self.ball.owner.clear()

        self.ball.last_touch = player

        self.ball.velocity_x = direction_x * 26

        self.ball.velocity_y = direction_y * 26

        self.ball.velocity_z = 3.5

    def finesse_shot(self, player, direction_x, direction_y):

        self.ball.owner.clear()

        self.ball.last_touch = player

        self.ball.velocity_x = direction_x * 15

        self.ball.velocity_y = direction_y * 15

        self.ball.velocity_z = 2.8