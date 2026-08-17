"""
BallControl.py
Điều khiển bóng
"""


class BallControl:

    def __init__(self, ball):

        self.ball = ball

    def attach(self, player):

        self.ball.owner.set_owner(player)

        self.ball.x = player.x

        self.ball.y = player.y

    def detach(self):

        self.ball.owner.clear()

    def update(self):

        if self.ball.owner.has_owner():

            owner = self.ball.owner.get_owner()

            self.ball.x = owner.x

            self.ball.y = owner.y