import pygame
import sys


from pygame.locals import *

from constants import *
from render import *
from gameboard import Gameboard
from blockpicker import BlockPicker

def init():
    pygame.init()
    surface = pygame.display.set_mode((650, 700))
    pygame.display.set_caption('SkyBlox')
    pygame.time.set_timer(USEREVENT+1, 1000)
    return surface

def control_block(event, surface, board):
    if event.key == K_UP or event.key == K_w:
        board.block.rotate(ROTATE_DIR)

    elif event.key == K_RIGHT or event.key == K_d:
        board.move_block(RIGHT)

    elif event.key == K_DOWN or event.key == K_s:
        board.block_fall()

    elif event.key == K_LEFT or event.key == K_a:
        board.move_block(LEFT)

    render_gameboard(surface, board)

def main():
    seconds = 0
    surface = init()

    clock = pygame.time.Clock()
    picker = BlockPicker(surface)

    render_screen(surface)
    board = Gameboard(picker.get_current())
    render_gameboard(surface,board)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == USEREVENT + 1:
                seconds += 1
                if board.block_fall() == False:
                    board.new_block(picker.pick_block())
                render_gameboard(surface, board)

                #print(seconds)

            if event.type == KEYDOWN:
                '''
                #Temporary code to test the block rotation
                if event.key == K_1:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = Block(BLOCK_T, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_2:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = Block(BLOCK_I, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_3:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = Block(BLOCK_L, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_4:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = Block(BLOCK_R, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_5:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = Block(BLOCK_O, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_6:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = Block(BLOCK_Z, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_7:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = Block(BLOCK_S, 0)
                    render_block(surface, 5, 4, tetromino)
                '''

                control_block(event, surface, board)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
