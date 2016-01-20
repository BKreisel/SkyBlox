import pygame
import sys

from pygame.locals import *


def init():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((600, 700))
    pygame.display.set_caption('SkyBlox')

def main():
    FPS = 30
    fpsClock = pygame.time.Clock()

    init()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
