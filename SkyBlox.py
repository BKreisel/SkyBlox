import pygame
import sys


from pygame.locals import *

from constants import *
from render import *
from gameboard import Gameboard
from blockpicker import BlockPicker
from scoreboard import Scoreboard

def init():
    pygame.init()
    surface = pygame.display.set_mode((650, 700))
    pygame.display.set_caption('SkyBlox')
    pygame.time.set_timer(USEREVENT+1, 1000)
    return surface

def control_block(event, surface, board):
    if event.key == K_UP or event.key == K_w:
        board.do_rotate(ROTATE_DIR)

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

    scoreboard = Scoreboard(surface)
    board = Gameboard(picker.get_current(),scoreboard)
    render_gameboard(surface,board)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == USEREVENT + 1:
                seconds += 1
                if board.block_fall() == False:
                    pygame.event.clear(KEYDOWN)
                    board.new_block(picker.pick_block())
                render_gameboard(surface, board)

                #print(seconds)

            if event.type == KEYDOWN:
                control_block(event, surface, board)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
