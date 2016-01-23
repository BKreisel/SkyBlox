from constants import *

class Block:
    def __init__(self, shape = [], orientation = 0):
        self.shape = shape
        self.orientation = orientation

    def rotate(self, dir):
        self.orientation = (self.orientation + dir) % len(self.shape)

    def get_pic(self):
        return self.shape[self.orientation]
