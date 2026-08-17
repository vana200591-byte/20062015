"""
BallBounce.py
Xử lý nảy bóng
"""


class BallBounce:

    def __init__(self, ball):

        self.ball = ball

        self.energy_loss = 0.55

    def bounce(self):

        if self.ball.z <= 0:

            self.ball.z = 0

            self.ball.velocity_z *= -self.energy_loss

    def set_energy_loss(self, value):

        self.energy_loss = value

    def update(self):

        self.bounce()