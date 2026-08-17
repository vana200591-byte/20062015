"""
Animation.py
Quản lý hoạt ảnh cầu thủ
"""


class Animation:

    def __init__(self):

        self.current = "Idle"

    def idle(self):

        self.current = "Idle"

    def walk(self):

        self.current = "Walk"

    def run(self):

        self.current = "Run"

    def sprint(self):

        self.current = "Sprint"

    def shoot(self):

        self.current = "Shoot"

    def pass_ball(self):

        self.current = "Pass"

    def header(self):

        self.current = "Header"

    def tackle(self):

        self.current = "Tackle"

    def celebrate(self):

        self.current = "Celebrate"

    def get(self):

        return self.current