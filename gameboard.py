from block import Block
from constants import *

class Gameboard:
    def __init__(self, first_tetro):
        self.block_x = 4
        self.block_y = 0
        self.tetromino = Block(first_tetro)

        self.gameboard = []
        for i in range (0,BOARD_CELL_HEIGHT):
            new = []
            for j in range (0,BOARD_CELL_WIDTH):
                new.append(0)
            self.gameboard.append(new)

    def move_block(self, dir):
        if(dir == RIGHT and self.block_x + len(self.tetromino.get_pic()[0])
        < BOARD_CELL_WIDTH):
            self.block_x += 1

        if(dir == LEFT and self.block_x > 0):
            self.block_x += dir

    def block_fall(self):
        if(self.block_y + len(self.tetromino.get_pic())
            < BOARD_CELL_HEIGHT):
            self.block_y += 1
