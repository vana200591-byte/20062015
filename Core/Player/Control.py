"""
Control.py
Xử lý điều khiển cầu thủ
"""


class Control:

    def __init__(self, player):

        self.player = player

    def move(self, dx, dy):

        self.player.move(dx, dy)

    def sprint(self):

        self.player.sprint()

    def stop_sprint(self):

        self.player.stop_sprint()

    def give_ball(self):

        self.player.give_ball()

    def remove_ball(self):

        self.player.remove_ball()

    def update(self):

        pass