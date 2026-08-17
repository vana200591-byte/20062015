"""
BallTrajectory.py
Quỹ đạo bóng
"""


class BallTrajectory:

    def __init__(self, ball):

        self.ball = ball

    def predict(self, frames=60):

        points = []

        x = self.ball.x
        y = self.ball.y
        z = self.ball.z

        vx = self.ball.velocity_x
        vy = self.ball.velocity_y
        vz = self.ball.velocity_z

        gravity = 0.35

        for _ in range(frames):

            x += vx
            y += vy
            z += vz

            vz -= gravity

            if z < 0:
                z = 0

            points.append((x, y, z))

        return points