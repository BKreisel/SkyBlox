import pygame

from constants import *

def render_title(surface):
    font = pygame.font.Font("assets/fonts/Exo-BoldItalic.otf",64)
    title_sky = font.render("Sky",True,WHITE)
    title_blox = font.render("Blox",True, WHITE)
    surface.blit(title_sky,(430,30))
    surface.blit(title_blox,(494,100))

def block_box(surface):
    pygame.draw.rect(surface, WHITE, (15, 30,400,640), 2)

def render_board(surface):

    items = [
        render_title
        ,block_box
    ]

    for item in items:
        item(surface)
