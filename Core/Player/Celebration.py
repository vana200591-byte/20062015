"""
Celebration.py
Ăn mừng sau khi ghi bàn
"""


class Celebration:

    def __init__(self, player):

        self.player = player

        self.current = None

    def normal(self):

        self.current = "Normal"

        print(f"{self.player.name} celebrates!")

    def knee_slide(self):

        self.current = "Knee Slide"

        print(f"{self.player.name} performs a knee slide!")

    def point_to_fans(self):

        self.current = "Point To Fans"

        print(f"{self.player.name} points to the fans!")

    def heart(self):

        self.current = "Heart"

        print(f"{self.player.name} makes a heart celebration!")

    def get(self):

        return self.current