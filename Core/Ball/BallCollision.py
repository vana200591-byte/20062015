"""
BallCollision.py
Va chạm bóng
"""


class BallCollision:

    def __init__(self, ball):

        self.ball = ball

    def hit_post(self):

        self.ball.velocity_x *= -0.8

        self.ball.velocity_y *= -0.8

        print("Ball hit the post!")

    def hit_player(self):

        self.ball.velocity_x *= 0.7

        self.ball.velocity_y *= 0.7

        print("Ball hit a player!")

    def out_of_field(self):

        self.ball.stop()

        print("Ball is out!")