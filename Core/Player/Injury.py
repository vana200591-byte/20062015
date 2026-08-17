"""
Injury.py
Quản lý chấn thương
"""


class Injury:

    def __init__(self):

        self.injured = False

        self.type = None

        self.recovery_time = 0

    def set_injury(self, injury_type, matches):

        self.injured = True

        self.type = injury_type

        self.recovery_time = matches

        print(f"Injury: {injury_type}")

    def recover_match(self):

        if self.recovery_time > 0:

            self.recovery_time -= 1

        if self.recovery_time == 0:

            self.injured = False

            self.type = None

    def is_injured(self):

        return self.injured