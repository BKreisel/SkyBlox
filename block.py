from constants import *

class Block:
    def __init__(self, shape = [], orientation = 0):
        print("New Block Created")
        self.shape = shape
        self.orientation = orientation
        self.color = pick_color(self.shape)

    def rotate(self, dir):
        self.orientation = (self.orientation + dir) % len(self.shape)

    def get_pic(self):
        return self.shape[self.orientation]
