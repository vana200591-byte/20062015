"""
BallCross.py
Tạt bóng
"""


class BallCross:

    def __init__(self, ball):

        self.ball = ball

    def cross(self, player, direction_x, direction_y):

        self.ball.owner.clear()

        self.ball.last_touch = player

        self.ball.velocity_x = direction_x * 14

        self.ball.velocity_y = direction_y * 14

        self.ball.velocity_z = 4.0

        print(f"{player.name} crosses the ball!")