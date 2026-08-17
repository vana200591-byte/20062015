"""
Header.py
Đánh đầu
"""


class Header:

    def __init__(self, player):

        self.player = player

    def attack_header(self):

        heading = self.player.attributes.heading

        print(f"{self.player.name} attacks with a header! Heading: {heading}")

    def defensive_header(self):

        heading = self.player.attributes.heading

        print(f"{self.player.name} clears the ball with a header! Heading: {heading}")

    def diving_header(self):

        print(f"{self.player.name} performs a diving header!")