import pygame
pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
CELL_SIZE = 200
board = [[None, None, None], [None, None, None], [None, None, None]]
player = 'X'
font = pygame.font.Font(None, 50)
game_over = False
winner = None
def draw_board():
    for row in range(3):
        for col in range(3):
            cell_pos_x = col * CELL_SIZE
            cell_pos_y = row * CELL_SIZE
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(cell_pos_x, cell_pos_y, CELL_SIZE, CELL_SIZE), 3)

            cell_value = board[row][col]
            if cell_value is not None:
                cell_text = font.render(cell_value, True, (255, 255, 255))
                cell_text_rect = cell_text.get_rect(center=(cell_pos_x + CELL_SIZE // 2, cell_pos_y + CELL_SIZE // 2))
                window.blit(cell_text, cell_text_rect)
def check_winner():
    global game_over, winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] is not None:
            winner = board[row][0]
            game_over = True
            return
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] is not None:
            winner = board[0][col]
            game_over = True
            return
    if board[0][0] == board[1][1] == board[2][2] is not None:
        winner = board[0][0]
        game_over = True
        return

    if board[0][2] == board[1][1] == board[2][0] is not None:
        winner = board[0][2]
        game_over = True
        return
    if all([cell is not None for row in board for cell in row]):
        game_over = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            cell_row = mouse_pos[1] // CELL_SIZE
            cell_col = mouse_pos[0] // CELL_SIZE
            if board[cell_row][cell_col] is None:
                board[cell_row][cell_col] = player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                check_winner()
    window.fill((0, 0, 0))
    draw_board()
    if game_over:
        if winner is not None:
            winner_text = font.render(f'Player {winner} wins!', True, (255, 255, 255))
        else:
            winner_text = font.render('It\'s a draw!', True, (255, 255, 255))
        winner_text_rect = winner_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(winner_text, winner_text_rect)
    pygame.display.update()
pygame.quit()
