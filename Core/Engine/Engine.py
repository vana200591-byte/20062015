from Config import *
from Logger import log

class Engine:

    def __init__(self):

        self.running = False

        self.fps = FPS

    def start(self):

        self.running = True

        log("Engine Started")

    def stop(self):

        self.running = False

        log("Engine Stopped")

    def update(self):

        if self.running:

            log("Updating...")