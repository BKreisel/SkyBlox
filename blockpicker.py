import render
import random

from constants import *

class BlockPicker():

    def __init__(self,surface):
        self.tetrominos = [
            BLOCK_I,BLOCK_L,BLOCK_T,BLOCK_R,BLOCK_O,BLOCK_Z,BLOCK_S
        ]
        self.surface = surface

        self.current = self.generate()
        self.next = self.generate()
        render.set_next_block_disp(surface,self.next)


    def generate(self):
        return self.tetrominos[random.randrange(0,len(self.tetrominos)-1)]

    def get_current(self):
        return self.current

    def get_next(self):
        return self.next

    def pick_block(self):
        self.current = self.next
        self.next = self.generate()
        render.set_next_block_disp(self.surface,self.next)
        return self.current
