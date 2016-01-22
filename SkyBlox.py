import pygame
import sys
from block import block

from pygame.locals import *

from constants import *
from render import *

def init():
    pygame.init()
    surface = pygame.display.set_mode((650, 700))
    pygame.display.set_caption('SkyBlox')
    pygame.time.set_timer(USEREVENT+1, 1000)
    return surface

def control_block(event, surface, tetromino,t_row,t_col):
    if event.key == K_UP or event.key == K_w:
        render_block(surface, t_row, t_col, tetromino, True)
        tetromino.rotate(ROTATE_DIR)
        render_block(surface, t_row, t_col, tetromino)
        print("Orientation: " + str(tetromino.orientation))
        print("Up")
    elif event.key == K_RIGHT or event.key == K_d:
        print("Right")
    elif event.key == K_DOWN or event.key == K_s:
        print("Down")
        render_block(surface, t_row, t_col, tetromino, True)
        render_block(surface, t_row+1, t_col, tetromino)
    elif event.key == K_LEFT or event.key == K_a:
        print("Left")


def main():
    seconds = 0
    clock = pygame.time.Clock()

    surface = init()
    render_screen(surface)

    #create a block
    tetromino = block(BLOCK_I, 0)
    t_row = 0
    t_col = BOARD_COLS / 2

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == USEREVENT + 1:
                seconds += 1
                render_block(surface, t_row, t_col,tetromino, True)
                t_row += 1
                render_block(surface, t_row, t_col, tetromino)

                print(seconds)

            if event.type == KEYDOWN:
                #Temporary code to test the block rotation
                if event.key == K_1:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = block(BLOCK_T, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_2:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = block(BLOCK_I, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_3:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = block(BLOCK_L, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_4:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = block(BLOCK_R, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_5:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = block(BLOCK_O, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_6:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = block(BLOCK_Z, 0)
                    render_block(surface, 5, 4, tetromino)
                if event.key == K_7:
                    render_block(surface, 5, 4, tetromino, True)
                    tetromino = block(BLOCK_S, 0)
                    render_block(surface, 5, 4, tetromino)

                control_block(event, surface, tetromino,t_row,t_col)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
