import pygame

from constants import *

def render_title(surface):
    font = pygame.font.Font("assets/fonts/Exo-BoldItalic.otf",64)
    title_sky = font.render("Sky",True,WHITE)
    title_blox = font.render("Blox",True, WHITE)
    surface.blit(title_sky,(430,30))
    surface.blit(title_blox,(494,100))

def block_box(surface):
    pygame.draw.rect(surface, WHITE, (BOARD_START_X - BOARD_BORDER, BOARD_START_Y - BOARD_BORDER, 400, 640), BOARD_BORDER)

def render_board(surface):

    items = [
        render_title
        ,block_box
    ]

    for item in items:
        item(surface)

def render_block(surface, row, col, block, isClear = False):
    color = WHITE
    if(isClear):
        color = BLACK

    #Loop through and display each sub block
    block_line = 0
    for line in block.get_pic():
        block_col = 0
        for piece in line:
            if piece != 0:
                pygame.draw.rect(surface, color, (BOARD_START_X + (col + block_col) *BLOCK_SIZE, BOARD_START_Y + (row + block_line) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            block_col += 1
        block_line += 1
