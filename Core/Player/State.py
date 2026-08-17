"""
State.py
Quản lý trạng thái cầu thủ
"""


class PlayerState:

    IDLE = "Idle"

    WALK = "Walk"

    RUN = "Run"

    SPRINT = "Sprint"

    PASS = "Pass"

    SHOOT = "Shoot"

    HEADER = "Header"

    TACKLE = "Tackle"

    DRIBBLE = "Dribble"

    CELEBRATE = "Celebrate"

    INJURED = "Injured"

    def __init__(self):

        self.current = PlayerState.IDLE

    def set(self, state):

        self.current = state

    def get(self):

        return self.current

    def reset(self):

        self.current = PlayerState.IDLE