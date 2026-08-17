"""
BallOwner.py
"""


class BallOwner:

    def __init__(self):

        self.player = None

    def set_owner(self, player):

        self.player = player

    def clear(self):

        self.player = None

    def has_owner(self):

        return self.player is not None

    def get_owner(self):

        return self.player

    def owner_name(self):

        if self.player is None:

            return "None"

        return self.player.name