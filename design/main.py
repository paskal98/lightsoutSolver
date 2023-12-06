import pygame, sys
from button import Button
import numpy as np


GRID_SIZE = 5  
CELL_SIZE = 80  

# Initialize the Lights Out board
board = np.random.randint(2, size=(GRID_SIZE, GRID_SIZE), dtype=bool)

# Initialize pygame
pygame.init()

current_index_algorithm = 0
current_index_board = 0 

ALGORITH_OPTIONS = ['DFS','GREEDY', 'A*']
BOARD_OPTIONS = [(2, 3), (5, 5)] 

# Create the game screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_board_size():
    return BOARD_OPTIONS[current_index_board]

def check_win(board):
    return np.all(board == False)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def draw_board(board, x_offset):
    border_width = 2
    rows, cols = board.shape  # Get the dimensions of the board
    global CELL_SIZE  # Declare CELL_SIZE as global to modify it

    rows, cols = get_board_size()  # Get the current board size
    if (rows, cols) == (2, 3):
        CELL_SIZE = 130  # Larger cell size for 2x3 board
    else:
        CELL_SIZE = 80   # Default cell size for other sizes

    for row in range(rows):
        for col in range(cols):
            color = "Yellow" if board[row, col] else "White"
            cell_rect = pygame.Rect(col * CELL_SIZE + 400 + x_offset, row * CELL_SIZE + 150, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, color, cell_rect)
            pygame.draw.rect(SCREEN, "Black", cell_rect, border_width)


def toggle_lights(grid, row, col):
    grid[row][col] = not grid[row][col]
    if row > 0:
        grid[row - 1][col] = not grid[row - 1][col]
    if row < len(grid) - 1:
        grid[row + 1][col] = not grid[row + 1][col]
    if col > 0:
        grid[row][col - 1] = not grid[row][col - 1]
    if col < len(grid[0]) - 1:
        grid[row][col + 1] = not grid[row][col + 1]







def play():
    rows, cols = get_board_size()  # Get the current board size
    board = np.random.randint(2, size=(rows, cols), dtype=bool)
    pygame.display.set_caption("Lights Out!")
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("LIGHTS OUT", True, "Yellow")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 90))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        if(current_index_board == 0):
            PLAY_BACK = Button(image=None, pos=(640, 599), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        else:
            PLAY_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        if(current_index_board == 0):
            PLAY_SOLVE = Button(image=None, pos=(640, 490), 
                            text_input="SOLVE", font=get_font(40), base_color="White", hovering_color="Red")
        else:
           PLAY_SOLVE = Button(image=None, pos=(640, 590), 
                            text_input="SOLVE", font=get_font(40), base_color="White", hovering_color="Green") 

        PLAY_SOLVE.changeColor(PLAY_MOUSE_POS)
        PLAY_SOLVE.update(SCREEN)

        # Shift the board to the right by 100 pixels
        draw_board(board, 39)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_SOLVE.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

                for row in range(GRID_SIZE):
                    for col in range(GRID_SIZE):
                        cell_rect = pygame.Rect(col * CELL_SIZE + 400 + 39, row * CELL_SIZE + 150, CELL_SIZE, CELL_SIZE)
                        if cell_rect.collidepoint(PLAY_MOUSE_POS):
                            toggle_lights(board, row, col)

                if check_win(board):
                    print("You won!")

        pygame.display.update()

    
def options():
    pygame.display.set_caption("Options!")
    global current_index_algorithm
    global current_index_board
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(36).render("SELECT ALGORITHM TO SOLVE GAME.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_ALGORITHM = Button(image=None, pos=(640, 260), 
                                text_input=ALGORITH_OPTIONS[current_index_algorithm], font=get_font(45), base_color="White", hovering_color="Green")
        
        OPTIONS_ALGORITHM.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_ALGORITHM.update(SCREEN)

        OPTIONS_TEXT_BOARD = get_font(50).render("SELECT BOARD", True, "White")
        OPTIONS_RECT_BOARD = OPTIONS_TEXT_BOARD.get_rect(center=(640, 360))
        SCREEN.blit(OPTIONS_TEXT_BOARD, OPTIONS_RECT_BOARD)
        
        OPTIONS_BOARD = Button(image=None, pos=(640, 460), 
                       text_input=str(BOARD_OPTIONS[current_index_board]), 
                       font=get_font(45), base_color="White", hovering_color="Green")
        
        OPTIONS_BOARD.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BOARD.update(SCREEN)
        
        OPTIONS_BACK = Button(image=None, pos=(640, 599), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                elif OPTIONS_ALGORITHM.checkForInput(OPTIONS_MOUSE_POS):
                    current_index_algorithm = (current_index_algorithm + 1) % len(ALGORITH_OPTIONS)
                    OPTIONS_ALGORITHM.text_input = ALGORITH_OPTIONS[current_index_algorithm]
                elif OPTIONS_BOARD.checkForInput(OPTIONS_MOUSE_POS):
                    current_index_board = (current_index_board + 1) % len(BOARD_OPTIONS)
                    OPTIONS_BOARD.text_input = BOARD_OPTIONS[current_index_board]

        pygame.display.update()


def main_menu():

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Lights Out", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
