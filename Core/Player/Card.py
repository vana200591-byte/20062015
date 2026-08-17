"""
Card.py
Quản lý thẻ phạt
"""


class Card:

    def __init__(self):

        self.yellow = 0

        self.red = False

    def give_yellow(self):

        self.yellow += 1

        print("Yellow Card!")

        if self.yellow >= 2:

            self.give_red()

    def give_red(self):

        self.red = True

        print("Red Card!")

    def clear(self):

        self.yellow = 0

        self.red = False

    def suspended(self):

        return self.red