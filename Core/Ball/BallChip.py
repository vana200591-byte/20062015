"""
BallChip.py
Bấm bóng
"""


class BallChip:

    def __init__(self, ball):

        self.ball = ball

    def chip(self, player, direction_x, direction_y):

        self.ball.owner.clear()

        self.ball.last_touch = player

        self.ball.velocity_x = direction_x * 8

        self.ball.velocity_y = direction_y * 8

        self.ball.velocity_z = 6.5

        print(f"{player.name} chips the ball!")