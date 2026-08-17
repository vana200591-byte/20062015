"""
BallPhysics.py
Xử lý vật lý của quả bóng
"""


class BallPhysics:

    def __init__(self, ball):

        self.ball = ball

        self.gravity = 0.35

        self.friction = 0.98

        self.air_resistance = 0.995

        self.bounce = 0.55

    def update(self):

        self.ball.velocity_z -= self.gravity

        self.ball.velocity_x *= self.air_resistance

        self.ball.velocity_y *= self.air_resistance

        self.ball.velocity_z *= self.air_resistance

        self.ball.x += self.ball.velocity_x

        self.ball.y += self.ball.velocity_y

        self.ball.z += self.ball.velocity_z

        if self.ball.z <= 0:

            self.ball.z = 0

            if abs(self.ball.velocity_z) > 0.2:

                self.ball.velocity_z *= -self.bounce

            else:

                self.ball.velocity_z = 0

        self.ball.velocity_x *= self.friction

        self.ball.velocity_y *= self.friction

    def kick(self, vx, vy, vz):

        self.ball.velocity_x = vx

        self.ball.velocity_y = vy

        self.ball.velocity_z = vz