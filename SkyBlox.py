import pygame
import sys

from pygame.locals import *

from constants import *
from render import *

def init():
    pygame.init()
    surface = pygame.display.set_mode((650, 700))
    pygame.display.set_caption('SkyBlox')
    pygame.time.set_timer(USEREVENT+1, 1000)
    return surface


def main():
    seconds = 0
    clock = pygame.time.Clock()

    surface = init()
    render_board(surface)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == USEREVENT + 1:
                seconds += 1
                print(seconds)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
