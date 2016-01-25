from constants import *

class Block:
    def __init__(self, shape = [], orientation = 0):
        self.shape = shape
        self.orientation = orientation

    def rotate(self, dir):
        self.orientation = (self.orientation + dir) % len(self.shape)

    def get_next_pic(self, dir):
        next_tetro = (self.orientation + dir) % len(self.shape)
        return self.shape[next_tetro]

    def get_pic(self):
        return self.shape[self.orientation]
