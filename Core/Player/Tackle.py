"""
Tackle.py
Xử lý xoạc bóng
"""


class Tackle:

    def __init__(self, player):

        self.player = player

        self.cooldown = 0

    def slide(self):

        if self.cooldown == 0:

            print(self.player.name, "performed a slide tackle!")

            self.cooldown = 60

    def update(self):

        if self.cooldown > 0:

            self.cooldown -= 1