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

def control_block(event, surface, tetromino):
    if event.key == K_UP or event.key == K_w:
        render_block(surface, 5, 4, tetromino, True)
        tetromino.rotate(ROTATE_DIR)
        render_block(surface, 5, 4, tetromino)
        print("Orientation: " + str(tetromino.orientation))
        print("Up")
    elif event.key == K_RIGHT or event.key == K_d:
        print("Right")
    elif event.key == K_DOWN or event.key == K_s:
        print("Down")
    elif event.key == K_LEFT or event.key == K_a:
        print("Left")


def main():
    seconds = 0
    clock = pygame.time.Clock()

    surface = init()
    render_board(surface)

    #create a block
    tetromino = block(BLOCK_I, 0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == USEREVENT + 1:
                seconds += 1
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

                control_block(event, surface, tetromino)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
