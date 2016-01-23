from block import Block
from constants import *

class Gameboard:
    def __init__(self, first_tetro):
        self.block_x = 4
        self.block_y = 0
        self.block = Block(first_tetro)

        self.gameboard = []
        for i in range (0,BOARD_CELL_HEIGHT):
            new = []
            for j in range (0,BOARD_CELL_WIDTH):
                new.append(0)
            self.gameboard.append(new)

    def move_block(self, dir):
        if(dir == RIGHT and self.block_x + len(self.block.get_pic()[0])
        < BOARD_CELL_WIDTH):
            self.block_x += 1

        if(dir == LEFT and self.block_x > 0):
            self.block_x += dir

    def new_block(self,new_tetro):
        self.block = Block(new_tetro)
        self.block_x =4
        self.block_y =0

    def block_fall(self):
        #self.print_gameboard()
        #print(self.did_vert_collide())
        if not self.did_vert_collide():
            self.block_y += 1
            return True
        else:
            self.add_to_board()
            return False

    def did_vert_collide(self):
        tetro = self.block.get_pic()
        rel_y = -1
        for cell in tetro:
            rel_y += 1
            rel_x = -1
            for val in cell:
                rel_x +=1
                x = self.block_x + rel_x
                y = self.block_y + rel_y
                if val > 0:
                    if y == 15:
                        return True
                    else:
                        if self.gameboard[y+1][x] > 0:
                            return True
        return False

    def add_to_board(self):

        rel_y = -1
        block = self.block.get_pic()
        for cell in block:
            rel_y += 1
            rel_x = -1
            for val in cell:
                rel_x +=1
                x = self.block_x + rel_x
                y = self.block_y + rel_y

                if val > 0:
                    self.gameboard[y][x] = val
        print(" ")
        self.print_gameboard()

    def print_gameboard(self):
        for line in self.gameboard:
            print(line)

    def get_pos(self, x, y):
        return self.gameboard[y][x]
