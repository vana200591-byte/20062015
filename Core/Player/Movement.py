"""
Movement.py
Điều khiển di chuyển cầu thủ
"""


class Movement:

    def __init__(self, player):

        self.player = player

    def move_up(self, speed):

        self.player.y -= speed

    def move_down(self, speed):

        self.player.y += speed

    def move_left(self, speed):

        self.player.x -= speed

    def move_right(self, speed):

        self.player.x += speed

    def sprint(self):

        self.player.is_sprinting = True

    def stop_sprint(self):

        self.player.is_sprinting = False

    def stop(self):

        self.player.is_running = False