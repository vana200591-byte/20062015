"""
Sprint.py
Quản lý tăng tốc của cầu thủ
"""


class Sprint:

    def __init__(self, player):

        self.player = player

        self.enabled = False

        self.speed_multiplier = 1.5

    def start(self):

        self.enabled = True

        print(f"{self.player.name} starts sprinting.")

    def stop(self):

        self.enabled = False

        print(f"{self.player.name} stops sprinting.")

    def get_speed(self):

        if self.enabled:

            return self.player.attributes.pace * self.speed_multiplier

        return self.player.attributes.pace