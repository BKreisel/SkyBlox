WHITE = (255,255,255)
BLACK = (0,0,0)
CYAN = (255,255,255)
PURPLE = (255,255,255)
ORANGE = (255,255,255)
BLUE = (255,255,255)
YELLOW = (255,255,255)
RED = (255,255,255)
GREEN = (255,255,255)

#Constants for the game
BOARD_START_X = 15
BOARD_START_Y = 30
BOARD_ROWS = 16
BOARD_COLS = 10
BOARD_BORDER = 2
CELL_SIZE = 40
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
                [[2,2,2], [0,2,0]],
                [[0,2], [2,2], [0,2]],
                [[0,2,0], [2,2,2]],
                [[2,0], [2,2], [2,0]]
            ]
BLOCK_L =   [
                [[3,0],[3,0],[3,3]],
                [[3,3,3], [3,0,0]],
                [[3,3],[0,3],[0,3]],
                [[0,0,3], [3,3,3]]
            ]
BLOCK_R =   [
                [[0,4],[0,4],[4,4]],
                [[4,0,0], [4,4,4]],
                [[4,4],[4],[4]],
                [[4,4,4], [0,0,4]]
            ]
BLOCK_O =   [
                [[5,5], [5,5]]
            ]
BLOCK_Z =   [
                [[0,6,6], [6,6,0]],
                [[6,0], [6,6], [0,6]]
            ]
BLOCK_S =   [
                [[7,7,0],[0,7,7]],
                [[0,7],[7,7],[7,0]]
            ]
