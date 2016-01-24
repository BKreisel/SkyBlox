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
        if(dir == RIGHT and self.did_horiz_collide() is not RIGHT):
            self.block_x += 1

        if(dir == LEFT and self.did_horiz_collide() is not LEFT):
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

    def did_horiz_collide(self):
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
                    if x == 0:
                        return LEFT
                    if x == 9:
                        return RIGHT
                    if self.gameboard[y][x+1] > 0:
                        return RIGHT
                    if self.gameboard[y][x-1] > 0:
                        return LEFT
        return False

    def drop_board(self,max_row):
        if max_row == 0:
            return
        for row in range(max_row,0,-1):
            for col in range(0,BOARD_CELL_WIDTH):
                self.gameboard[row][col] = self.gameboard[row-1][col]
        #Clear the first row
        self.destroy_line(0)



    def destroy_line(self,row):
        for col in range(0, BOARD_CELL_WIDTH):
            self.gameboard[row][col] = 0
        self.drop_board(row)

    def clear_line(self):
        for row in range(0,BOARD_CELL_HEIGHT):
            for col in range(0,BOARD_CELL_WIDTH):
                if self.get_pos(col,row) == 0:
                    print("Breaking: (" + str(row) + "," + str(col) + ")")
                    break
                if col == BOARD_CELL_WIDTH - 1:
                    print("Detroying row: " + str(row))
                    self.destroy_line(row)



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
        self.print_gameboard()

        #if a line is complete, destory it.
        self.clear_line()
        print()
        self.print_gameboard()

    def print_gameboard(self):
        for line in self.gameboard:
            print(line)

    def get_pos(self, x, y):
        return self.gameboard[y][x]
