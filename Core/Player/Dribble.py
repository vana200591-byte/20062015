"""
Dribble.py
Rê bóng
"""


class Dribble:

    def __init__(self, player):

        self.player = player

    def dribble_forward(self):

        self.player.x += 2

        print(f"{self.player.name} dribbles forward.")

    def turn_left(self):

        print(f"{self.player.name} turns left.")

    def turn_right(self):

        print(f"{self.player.name} turns right.")

    def stop_ball(self):

        print(f"{self.player.name} stops the ball.")

    def skill_move(self):

        print(f"{self.player.name} performs a skill move!")