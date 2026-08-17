"""
Player.py
Lớp cầu thủ cơ bản của Football Game v0.4
"""

from Player.Attributes import Attributes


class Player:

    def __init__(self, name="Unknown"):

        self.name = name

        self.number = 0

        self.team = None

        self.position = "ST"

        self.attributes = Attributes()

        self.x = 0.0
        self.y = 0.0

        self.direction = 0

        self.has_ball = False

        self.is_running = False

        self.is_sprinting = False

        self.is_injured = False

        self.yellow_cards = 0

        self.red_card = False

    def move(self, dx, dy):

        self.x += dx

        self.y += dy

    def give_ball(self):

        self.has_ball = True

    def remove_ball(self):

        self.has_ball = False

    def sprint(self):

        self.is_sprinting = True

    def stop_sprint(self):

        self.is_sprinting = False

    def update(self):

        pass

    def __str__(self):

        return f"{self.name} ({self.position})"