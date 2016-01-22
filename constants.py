WHITE = (255,255,255)
BLACK = (0,0,0)

#Constants for the game
BOARD_START_X = 15
BOARD_START_Y = 30
BOARD_ROWS = 16
BOARD_COLS = 10
BOARD_BORDER = 2
BLOCK_SIZE = 40
ROTATE_DIR = 1
BOARD_WIDTH = 400
BOARD_HEIGHT = 640
BOARD_CELL_WIDTH = 10
BOARD_CELL_HEIGHT = 16
LEFT = -1
RIGHT = 1

#Types of Blocks
BLOCK_I =   [
                [[1,1,1,1]],
                [[1],[1],[1],[1]]
            ]

BLOCK_T =   [
                [[1,1,1], [0,1,0]],
                [[0,1], [1,1], [0,1]],
                [[0,1,0], [1,1,1]],
                [[1,0], [1,1], [1,0]]
            ]
BLOCK_L =   [
                [[1,0],[1,0],[1,1]],
                [[1,1,1], [1,0,0]],
                [[1,1],[0,1],[0,1]],
                [[0,0,1], [1,1,1]]
            ]
BLOCK_R =   [
                [[0,1],[0,1],[1,1]],
                [[1,0,0], [1,1,1]],
                [[1,1],[1],[1]],
                [[1,1,1], [0,0,1]]
            ]
BLOCK_O =   [
                [[1,1], [1,1]]
            ]
BLOCK_Z =   [
                [[0,1,1], [1,1,0]],
                [[1,0], [1,1], [0,1]]
            ]
BLOCK_S =   [
                [[1,1,0],[0,1,1]],
                [[0,1],[1,1],[1,0]]
            ]
