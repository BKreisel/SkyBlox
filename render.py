import pygame

from constants import *

def title(surface):
    font = pygame.font.Font("assets/fonts/Exo-BoldItalic.otf",64)
    title_sky = font.render("Sky",True,WHITE)
    title_blox = font.render("Blox",True, WHITE)
    surface.blit(title_sky,(430,30))
    surface.blit(title_blox,(494,100))

def set_game_info(surface,level_val=1,score_val=0,lines_val=0):
    font_size = 32
    font = pygame.font.Font("assets/fonts/Exo-BoldItalic.otf",font_size)

    level_text = "Level: " + str(level_val)
    score_text = "Score: " + str(score_val)
    lines_text = "Lines: " + str(lines_val)

    level = font.render(level_text,True,WHITE)
    score = font.render(score_text,True, WHITE)
    lines = font.render(lines_text,True, WHITE)

    cover_x = lambda text: len(text) * font_size

    #(Re)draw LEVEL
    pygame.draw.rect(surface,BLACK,(430,500,cover_x(level_text),font_size+3))
    surface.blit(level,(430,500))

    #(Re)draw SCORE
    pygame.draw.rect(surface,BLACK,(430,550,cover_x(score_text),font_size+3))
    surface.blit(score,(430,550))

    #(Re)draw LINES
    pygame.draw.rect(surface,BLACK,(430,600,cover_x(lines_text),font_size+3))
    surface.blit(lines,(430,600))

def game_border(surface):
    pygame.draw.rect(surface, WHITE,
        (BOARD_START_X - BOARD_BORDER, BOARD_START_Y - BOARD_BORDER, 400, 640),
         BOARD_BORDER)

def render_screen(surface):

    items = [
        title,
        game_border,
        set_game_info,
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
                pygame.draw.rect(surface, color,
                    (BOARD_START_X + (col + block_col) *BLOCK_SIZE,
                    BOARD_START_Y + (row + block_line) * BLOCK_SIZE,
                    BLOCK_SIZE, BLOCK_SIZE))
            block_col += 1
        block_line += 1
