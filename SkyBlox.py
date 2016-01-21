import pygame
import sys

from pygame.locals import *


def init():
    pygame.init()
    pygame.draw.rect(surface, (255,255,255), (15, 30,400,640), 2)
    pygame.display.set_caption('SkyBlox')
    pygame.time.set_timer(USEREVENT+1, 1000)


def main():
    seconds = 0
    clock = pygame.time.Clock()

    init()

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
