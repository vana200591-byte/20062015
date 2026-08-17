"""
BallState.py
"""


class BallState:

    FREE = "FREE"

    CONTROLLED = "CONTROLLED"

    PASSING = "PASSING"

    SHOOTING = "SHOOTING"

    CROSSING = "CROSSING"

    IN_AIR = "IN_AIR"

    OUT = "OUT"

    GOAL = "GOAL"

    def __init__(self):

        self.current = BallState.FREE

    def set(self, state):

        self.current = state

    def get(self):

        return self.current

    def reset(self):

        self.current = BallState.FREE