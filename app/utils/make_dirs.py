import os
class Make:
    def __init__(self, path):
        self.path = path

    def make(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)