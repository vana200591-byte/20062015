"""
BallSound.py
Quản lý âm thanh của bóng
"""


class BallSound:

    def __init__(self):

        self.volume = 100

    def kick(self):

        print("Play: kick.wav")

    def pass_ball(self):

        print("Play: pass.wav")

    def shoot(self):

        print("Play: shoot.wav")

    def bounce(self):

        print("Play: bounce.wav")

    def hit_post(self):

        print("Play: post.wav")

    def goal(self):

        print("Play: goal.wav")

    def whistle(self):

        print("Play: whistle.wav")