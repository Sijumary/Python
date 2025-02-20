import pygame
import random

pygame.init()
WIDTH = 600
HEIGHT = 600
BACKGROUND_COLOR = (40, 40, 40)
LINE_COLOR = (70, 70, 70)
CELL_SIZE = WIDTH // 3

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-tc-Toe")


PLAYER_SYMBOL = "X"
AI_SYMBOL = "O"
PLAYER_COLOR = (0, 255, 0)
AI_COLOR = (255, 0, 0)
EMPTY_COLOR = (0, 0, 0)

board = [[""for _ in range(3)] for _ in range(3)]
turn = "player"
game_over = False
winner = None

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_COLOR = (50, 50, 50)
BUTTON_TEXT_COLOR = (255, 255,255)
BUTTON_FONT = pygame.font.Font(None, 30)

reset_buttonrect = pygame.Rect(
    (WIDTH - BUTTON_WIDTH) // 2,
    (HEIGHT - BUTTON_HEIGHT) // 2,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
)
# Helper functions
def draw_board():
    # Draw the game board
    win.fill(BACKGROUND_COLOR)

    # Draw vertical lines
    for x in range(1, 3):
        pygame.draw.line(
            win, LINE_COLOR, (CELL_SIZE * x, 0), (CELL_SIZE * x, HEIGHT), 2
        )

    # Draw horizontal lines
    for y in range(1, 3):
        pygame.draw.line(win, LINE_COLOR, (0, CELL_SIZE * y), (WIDTH, CELL_SIZE * y), 2)

def draw_symbols():
    # Draw the player and AI symbols on the game board
    for x in range(3):
        for y in range(3):
            symbol = board[x][y]
            if symbol == PLAYER_SYMBOL:
                color = PLAYER_COLOR
            elif symbol == AI_SYMBOL:
                color = AI_COLOR
            else:
                color = EMPTY_COLOR
            if symbol != "":
                pygame.draw.circle(
                    win,
                    color,
                    (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),
                    CELL_SIZE // 2 - 10,
                    2,
                )

def is_board_full():
    # Check if the game board is full
    for row in board:
        if "" in row:
            return False
    return True

def is_winner(symbol):
    # Check if a player has won the game
      for row in board:
        if all(cell == symbol for cell in row):
            return True
      for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
      if all(board[i][i] == symbol for i in range(3)):
        return True
      if all(board[i][2 - i] == symbol for i in range(3)):
        return True
      return False

def make_move(x, y, symbol):
    # Make a move on the game board
    if board[x][y] == "":
        board[x][y] = symbol
        return True
    return False


def player_move():
    # Handle the player's move
    global turn
    mouse_pos = pygame.mouse.get_pos()
    cell_x = mouse_pos[0] // CELL_SIZE
    cell_y = mouse_pos[1] // CELL_SIZE

    if make_move(cell_x, cell_y, PLAYER_SYMBOL):
        turn = "ai"

def ai_move():
    # Handle the AI's move
    global turn
    empty_cells = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == "":
                empty_cells.append((x, y))

    if empty_cells:
        x, y = random.choice(empty_cells)
        make_move(x, y, AI_SYMBOL)

    turn = "player"

def check_game_over():
    # Check if the game is over
    global game_over, winner
    if is_winner(PLAYER_SYMBOL):
        game_over = True
        return "player"
    elif is_winner(AI_SYMBOL):
        game_over = True
        return "ai"
    elif is_board_full():
        game_over = True
        return "tie"
    return None

def draw_winner():
    # Draw the winner message on the window
    font = pygame.font.Font(None, 50)
    if winner == "player":
        text = font.render("Player Wins!", True, PLAYER_COLOR)
    elif winner == "ai":
        text = font.render("AI Wins!", True, AI_COLOR)
    else:
        text = font.render("It's a Tie!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    win.blit(text, text_rect)

def draw_reset_button():
    # Draw the reset button on the window
    pygame.draw.rect(win, BUTTON_COLOR, reset_button_rect)
    button_text = BUTTON_FONT.render("Reset", True, BUTTON_TEXT_COLOR)
    button_text_rect = button_text.get_rect(center=reset_button_rect.center)
    win.blit(button_text, button_text_rect)

def reset_game():
    # Reset the game state
    global board, turn, game_over, winner
    board = [["" for _ in range(3)] for _ in range(3)]
    turn = "player"
    game_over = False
    winner = None
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button_rect.collidepoint(event.pos):
                reset_game()
            elif not game_over and turn == "player":
                player_move()

    if not game_over and turn == "ai":
        ai_move()
        check_game_over()

    draw_board()
    draw_symbols()

    if game_over:
        draw_winner()
        draw_reset_button()

    pygame.display.flip()

# Quit the game
pygame.quit()
