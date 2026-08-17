"""
Health.py
Quản lý HP và chấn thương
"""


class Health:

    def __init__(self, max_health=100):

        self.max_health = max_health

        self.current = max_health

        self.injured = False

    def damage(self, amount):

        self.current -= amount

        if self.current < 0:

            self.current = 0

    def heal(self, amount):

        self.current += amount

        if self.current > self.max_health:

            self.current = self.max_health

    def set_injury(self):

        self.injured = True

    def recover(self):

        self.injured = False

    def is_alive(self):

        return self.current > 0