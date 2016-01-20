import pygame
import sys

from pygame.locals import *


def init():
    pygame.init()
    surface = pygame.display.set_mode((600, 700))
    pygame.draw.rect(surface, (255,255,255), (15, 30,400,640), 2)
    pygame.display.set_caption('SkyBlox')

def gameLoop(board):


    #Move Block
    #Process

    print("Test")

def main():
    FPS = 30
    fpsClock = pygame.time.Clock()

    init()

    board = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
