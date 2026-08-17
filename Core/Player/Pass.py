"""
Pass.py
Xử lý chuyền bóng
"""


class Pass:

    def __init__(self, player):

        self.player = player

    def short_pass(self):

        power = self.player.attributes.short_pass

        print(f"{self.player.name} makes a short pass. Power: {power}")

    def long_pass(self):

        power = self.player.attributes.long_pass

        print(f"{self.player.name} makes a long pass. Power: {power}")

    def through_pass(self):

        vision = self.player.attributes.vision

        print(f"{self.player.name} makes a through pass. Vision: {vision}")

    def cross(self):

        crossing = self.player.attributes.crossing

        print(f"{self.player.name} crosses the ball. Crossing: {crossing}")