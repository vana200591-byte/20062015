"""
BallAnimation.py
Hoạt ảnh quay của bóng
"""


class BallAnimation:

    def __init__(self, ball):

        self.ball = ball

        self.rotation = 0.0

    def update(self):

        speed = abs(self.ball.velocity_x) + abs(self.ball.velocity_y)

        self.rotation += speed * 4

        if self.rotation >= 360:

            self.rotation -= 360

    def reset(self):

        self.rotation = 0.0