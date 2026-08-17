"""
Goalkeeper.py
Lớp thủ môn kế thừa Player
"""

from Player.Player import Player


class Goalkeeper(Player):

    def __init__(self, name="Goalkeeper"):

        super().__init__(name)

        self.position = "GK"

        self.reflex = 70
        self.diving = 70
        self.handling = 70
        self.kicking = 70
        self.positioning = 70

    def dive(self):

        print(self.name, "dives!")

    def catch_ball(self):

        self.has_ball = True

        print(self.name, "caught the ball!")

    def punch_ball(self):

        self.has_ball = False

        print(self.name, "punched the ball!")

    def goal_kick(self):

        print(self.name, "takes a goal kick.")

    def update(self):

        pass