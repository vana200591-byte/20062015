"""
Stamina.py
Quản lý thể lực cầu thủ
"""


class Stamina:

    def __init__(self, max_stamina=100):

        self.max_stamina = max_stamina

        self.current = max_stamina

    def decrease(self, amount):

        self.current -= amount

        if self.current < 0:

            self.current = 0

    def recover(self, amount):

        self.current += amount

        if self.current > self.max_stamina:

            self.current = self.max_stamina

    def is_tired(self):

        return self.current <= 20

    def reset(self):

        self.current = self.max_stamina