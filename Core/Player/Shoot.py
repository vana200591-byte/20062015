"""
Shoot.py
Xử lý sút bóng
"""


class Shoot:

    def __init__(self, player):

        self.player = player

        self.power = 0

    def normal_shot(self):

        self.power = self.player.attributes.shooting

        print(self.player.name, "shoots!")

    def finesse_shot(self):

        self.power = self.player.attributes.curve

        print(self.player.name, "takes a finesse shot!")

    def power_shot(self):

        self.power = self.player.attributes.shooting + 20

        print(self.player.name, "takes a power shot!")

    def chip_shot(self):

        self.power = self.player.attributes.finishing

        print(self.player.name, "chips the goalkeeper!")