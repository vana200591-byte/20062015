import time


class GameTime:

    def __init__(self):

        self.delta = 0

        self.last = time.time()

    def update(self):

        now = time.time()

        self.delta = now - self.last

        self.last = now

        return self.delta