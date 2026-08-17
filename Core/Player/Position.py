"""
Position.py
Quản lý vị trí trên sân
"""


class Position:

    GK = "Goalkeeper"

    LB = "Left Back"

    CB = "Center Back"

    RB = "Right Back"

    CDM = "Defensive Midfielder"

    CM = "Center Midfielder"

    CAM = "Attacking Midfielder"

    LW = "Left Winger"

    RW = "Right Winger"

    ST = "Striker"

    CF = "Center Forward"

    def __init__(self, position=ST):

        self.position = position

    def set_position(self, position):

        self.position = position

    def get_position(self):

        return self.position