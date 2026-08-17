"""
Skills.py
Kỹ năng rê bóng của cầu thủ
"""


class Skills:

    def __init__(self, player):

        self.player = player

    def roulette(self):

        print(self.player.name, "performed Roulette.")

    def step_over(self):

        print(self.player.name, "performed Step Over.")

    def rainbow(self):

        print(self.player.name, "performed Rainbow Flick.")

    def body_feint(self):

        print(self.player.name, "performed Body Feint.")

    def heel_to_heel(self):

        print(self.player.name, "performed Heel To Heel.")

    def fake_shot(self):

        print(self.player.name, "performed Fake Shot.")