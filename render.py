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

def set_next_block_disp(surface,tetromino=None):
    font_size = 32
    font = pygame.font.Font("assets/fonts/Exo-BoldItalic.otf",font_size)
    next_text = font.render("Next Block",True,WHITE)
    surface.blit(next_text,(430,250))

    if tetromino:
        pygame.draw.rect(surface,BLACK,(450,300,CELL_SIZE*4,CELL_SIZE*4))
        row = -1
        for line in tetromino[0]:
            row += 1
            col = -1
            for cell in line:
                col += 1
                if cell > 0:
                    cell_coords = (
                        450 + (col*CELL_SIZE),
                        300 +(row*CELL_SIZE),
                        CELL_SIZE,CELL_SIZE,
                    )
                    pygame.draw.rect(surface,COLOR_LIST[cell],cell_coords)

def game_border(surface):
    pygame.draw.rect(surface, WHITE,
        (BOARD_START_X - BOARD_BORDER, BOARD_START_Y - BOARD_BORDER,
         BOARD_WIDTH + BOARD_BORDER + BOARD_BORDER / 2,
         BOARD_HEIGHT + BOARD_BORDER + BOARD_BORDER / 2),
         BOARD_BORDER)

def render_screen(surface):

    items = [
        title,
        game_border,
        set_game_info,
        set_next_block_disp,
    ]

    for item in items:
        item(surface)

def render_block(surface, row, col, block, color = BLACK):
    #Loop through and display each sub block
    block_line = 0
    for line in block.get_pic():
        block_col = 0
        for piece in line:
            if piece != 0:
                pygame.draw.rect(surface, color,
                    (BOARD_START_X + (col + block_col) * CELL_SIZE,
                    BOARD_START_Y + (row + block_line) * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE))
            block_col += 1
        block_line += 1

def render_borders(surface):
    for row in range(0,BOARD_CELL_HEIGHT):
        for col in range(0,BOARD_CELL_WIDTH):
            pygame.draw.rect(surface, BLACK,
                             (BOARD_START_X + col * CELL_SIZE,
                              BOARD_START_Y + row * CELL_SIZE,
                              CELL_SIZE, CELL_SIZE), 1)

def render_gameboard(surface, field):

    pos_y = 0
    for row in field.gameboard:
        pos_x = 0
        for col in row:
            pygame.draw.rect(surface, COLOR_LIST[field.get_pos(pos_x, pos_y)],
                             (BOARD_START_X + pos_x * CELL_SIZE,
                              BOARD_START_Y + pos_y * CELL_SIZE,
                              CELL_SIZE, CELL_SIZE))
            pos_x += 1
        pos_y += 1

    curr_col = 0
    for cell in field.block.get_pic()[0]:
        if cell != 0:
            curr_col = cell

    render_block(surface, field.block_y, field.block_x, field.block,
                 COLOR_LIST[curr_col])
    render_borders(surface)
