import pygame, sys
from button import Button
import numpy as np
from event_bus import EventBus
import time
from main.algorithmus.A_start.a_star import AStar
from main.algorithmus.bfs.bfs import BreathFirstSearch

from main.algorithmus.dfs.dfs import DeepFirstSearch
from main.algorithmus.greedy.greedy import GreedySearch

COL = 5
ROW = 5
CELL_SIZE = 80

event_bus = EventBus()

pygame.init()

current_index_algorithm = 3
current_index_board = 1
show_solution = False
toggled = []
ALGORITH_OPTIONS = ['BFS','DFS','GREEDY', 'A*']
BOARD_OPTIONS = [(2, 3), (5, 5)]
current_index_map_2x3 = 0
current_index_map_5x5 = 0

BOARD_2x3_NAME = ["1 (2x3)", "2 (2x3)", "3 (2x3)", "4 (2x3)"]
BOARD_5x5_NAME = ["1 (5x5)", "2 (5x5)", "3 (5x5)", "4 (5x5)","5 (5x5)","6 (5x5)"]

BOARD_2x3 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0]
]

BOARD_5x5 = [
    [
        1, 1, 0, 1, 1,
        1, 0, 0, 0, 1,
        0, 0, 0, 0, 0,
        1, 0, 0, 0, 1,
        1, 1, 0, 1, 1

    ],
    [
        1, 1, 0, 0, 0,
        1, 0, 1, 0, 1,
        0, 1, 1, 0, 1,
        0, 0, 1, 0, 1,
        0, 0, 0, 0, 0

    ],
    [
        1, 1, 0, 0, 0,
        1, 1, 0, 0, 0,
        0, 0, 1, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0

    ],
    [
        1, 1, 0, 0, 0,
        1, 1, 0, 0, 0,
        0, 0, 1, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0

    ],
    [
        1, 1, 0, 1, 1,
        1, 1, 0, 1, 1,
        0, 0, 0, 0, 0,
        1, 1, 0, 1, 1,
        1, 1, 0, 1, 1

    ],
    [
        0, 0, 1, 0, 0,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        0, 0, 1, 0, 0

    ]
]

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

def handle_game_event(enteredArray):
    global board
    npArr = np.array(enteredArray)
    if (current_index_board == 0):
        board = npArr.reshape(2, 3)
    else:
        board = npArr.reshape(ROW, COL)
    # delay_seconds = 0.1
    # time.sleep(delay_seconds)
    draw_board(board, 400)
    pygame.display.update()


def solveMap(rows, cols, board_1d):
    global current_index_algorithm
    global board
    global show_solution
    global toggled
    if(current_index_algorithm == 0):
        bfs = BreathFirstSearch(rows, cols, board_1d, event_bus=event_bus)
        execution_time, toggle_combination, _ = bfs.solve()
    elif(current_index_algorithm == 1):
        dfs = DeepFirstSearch(rows, cols, board_1d, event_bus=event_bus)
        time, toggle_combination, queue_solution = dfs.solve()
    elif(current_index_algorithm == 2):
        greedy = GreedySearch(rows, cols, board_1d, event_bus=event_bus)
        time, toggle_combination, _ = greedy.solve()
    elif(current_index_algorithm == 3):
        aStar = AStar(rows, cols, board_1d, event_bus)
        execution_time, toggle_combination, _ = aStar.solve()
    toggled = toggle_combination
    print(toggled)
    show_solution = True
    

def draw_solution_board(board, x_offset):
    global CELL_SIZE
    global toggled

    border_width = 2
    rows, cols = board.shape
    
    rows, cols = get_board_size()
    toggledMap = np.array(toggled, dtype=bool).reshape(rows, cols)
    if (rows, cols) == (2, 3):
        CELL_SIZE = 130
    else:
        CELL_SIZE = 80
    for row in range(rows):
        for col in range(cols):
            color = "Yellow" if board[row, col] else "White"
            l = color
            color = "Green" if toggledMap[row, col] else l
            cell_rect = pygame.Rect(col * CELL_SIZE + 400 + x_offset, row * CELL_SIZE + 150, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, color, cell_rect)
            pygame.draw.rect(SCREEN, "Black", cell_rect, border_width)

def draw_board(board, x_offset):
    border_width = 2
    rows, cols = board.shape
    global CELL_SIZE

    rows, cols = get_board_size()
    if (rows, cols) == (2, 3):
        CELL_SIZE = 130
    else:
        CELL_SIZE = 80

    for row in range(rows):
        for col in range(cols):
            color = "Yellow" if board[row, col] else "White"
            cell_rect = pygame.Rect(col * CELL_SIZE + 400 + x_offset, row * CELL_SIZE + 150, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, color, cell_rect)
            pygame.draw.rect(SCREEN, "Black", cell_rect, border_width)

def toggle_lights(grid, row, col):
    global show_solution
    global toggled
    if show_solution:
        rows, cols = grid.shape
        if 0 <= row < rows and 0 <= col < cols:
            toggledMap = np.array(toggled, dtype=bool).reshape(rows, cols)
            toggledMap[row][col] = False
            toggled = toggledMap.astype(int).flatten().tolist()

    rows, cols = len(grid), len(grid[0])
    if 0 <= row < rows and 0 <= col < cols:
        grid[row][col] = not grid[row][col]
        if row > 0:
            grid[row - 1][col] = not grid[row - 1][col]
        if row < rows - 1:
            grid[row + 1][col] = not grid[row + 1][col]
        if col > 0:
            grid[row][col - 1] = not grid[row][col - 1]
        if col < cols - 1:
            grid[row][col + 1] = not grid[row][col + 1]



def get_map_data():
    global current_index_map_5x5
    global current_index_map_2x3
    global toggled
    global show_solution
    toggled = []
    show_solution = False
    if get_board_size()==(2,3):
        init_field = BOARD_2x3[current_index_map_2x3]
        return np.array(init_field, dtype=bool).reshape(2, 3) , (np.array(init_field).reshape(2, 3)).astype(int).flatten().tolist()
    else:
        init_field = BOARD_5x5[current_index_map_5x5]
        return np.array(init_field, dtype=bool).reshape(5, 5), (np.array(init_field).reshape(5, 5)).astype(int).flatten().tolist()


def play():
    global show_solution
    start_time = None
    timer_running = False
    elapsed_time = 0
    pygame.display.set_caption("Lights Out!")
    rows, cols = get_board_size()  
    board, board_1d = get_map_data()
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("LIGHTS OUT", True, "Yellow")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 90))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        if(current_index_board == 0):
            PLAY_MAP = get_font(20).render("INITIAL MAP", True, "Yellow")
            PLAY_MAAP = PLAY_MAP.get_rect(center=(300, 450))
            SCREEN.blit(PLAY_MAP, PLAY_MAAP)

            PLAY_SOLVE = get_font(20).render("SOLVER", True, "Yellow")
            PLAY_SOLVER = PLAY_SOLVE.get_rect(center=(1000, 450))
            PLAY_SOLVER = PLAY_SOLVE.get_rect(center=(1000, 450))
            SCREEN.blit(PLAY_SOLVE, PLAY_SOLVER)
        else:
            PLAY_MAP = get_font(20).render("INITIAL MAP", True, "Yellow")
            PLAY_MAAP = PLAY_MAP.get_rect(center=(300, 590))
            SCREEN.blit(PLAY_MAP, PLAY_MAAP)

            PLAY_SOLVE = get_font(20).render("SOLVER", True, "Yellow")
            PLAY_SOLVER = PLAY_SOLVE.get_rect(center=(1000, 590))
            PLAY_SOLVER = PLAY_SOLVE.get_rect(center=(1000, 590))
            SCREEN.blit(PLAY_SOLVE, PLAY_SOLVER)

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
                            text_input="SOLVE", font=get_font(40), base_color="White", hovering_color="Red")

        PLAY_SOLVE.changeColor(PLAY_MOUSE_POS)
        PLAY_SOLVE.update(SCREEN)

        draw_board(board, -300) if show_solution == False else draw_solution_board(board,-300)

        draw_board(board, 400) if show_solution == False else draw_board(np.full((rows, cols), False), 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_SOLVE.checkForInput(PLAY_MOUSE_POS):
                    start_time = time.time()
                    timer_running = True
                    event_bus.subscribe('test', handle_game_event)
                    solveMap(rows, cols, board_1d)
                for row in range(ROW):
                    for col in range(COL):
                        x_pos = col * CELL_SIZE + 400 - 300  # Adjust for the left offset
                        y_pos = row * CELL_SIZE + 150
                        cell_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
                        if cell_rect.collidepoint(PLAY_MOUSE_POS):
                            toggle_lights(board, row, col)
            if timer_running:
                elapsed_time = time.time() - start_time

            if show_solution:
                timer_running = False

            # Display the timer
            timer_text = get_font(20).render(f"Time: {elapsed_time:.2f} seconds", True, "White")
            timer_rect = timer_text.get_rect(center=(1000, 130))
            SCREEN.blit(timer_text, timer_rect)

            pygame.display.update()


def options():
    pygame.display.set_caption("Options!")
    global current_index_algorithm
    global current_index_board
    global toggled
    global show_solution
    while True:
        toggled = []
        show_solution = False
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


def select_map():

    pygame.display.set_caption("Maps!")
    global current_index_map_2x3
    global current_index_map_5x5
    global toggled
    global show_solution

    while True:
        toggled = []
        show_solution = False
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(36).render("SELECT MAP", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        if get_board_size() == (2, 3):
            map_names = BOARD_2x3_NAME
            current_index_map = current_index_map_2x3
        else:
            map_names = BOARD_5x5_NAME
            current_index_map = current_index_map_5x5

        OPTIONS_ALGORITHM = Button(image=None, pos=(640, 260),
                                   text_input=map_names[current_index_map], font=get_font(45),
                                   base_color="White", hovering_color="Green")

        OPTIONS_ALGORITHM.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_ALGORITHM.update(SCREEN)

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
                    if get_board_size() == (2, 3):
                        current_index_map_2x3 = (current_index_map_2x3 + 1) % len(BOARD_2x3_NAME)
                        OPTIONS_ALGORITHM.text_input = BOARD_2x3_NAME[current_index_map_2x3]
                    else:
                        current_index_map_5x5 = (current_index_map_5x5 + 1) % len(BOARD_5x5_NAME)
                        OPTIONS_ALGORITHM.text_input = BOARD_5x5_NAME[current_index_map_5x5]

        pygame.display.update()




def main_menu():


    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Lights Out", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(420, 250),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        MAP_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(900, 250),
                            text_input="MAP", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, MAP_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if MAP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select_map()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()