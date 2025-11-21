import pygame
import random

WIDTH, HEIGHT = 800, 600
BOX_SIZE = 100
FPS = 0
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ashta Cheamma")

def drawBoard(board):
    WIN.fill((255, 255, 255))
    pygame.draw.rect(WIN, (255, 0, 0), board, 2)
    cols = 5
    rows = 5
    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(WIN, (0, 0, 0),
                             (board.x + j*BOX_SIZE, board.y + i*BOX_SIZE, BOX_SIZE, BOX_SIZE), 1)
            if (i, j) in {(0,2),(4,2),(2,0),(2,4),(2,2)}:
                pygame.draw.line(WIN, (255, 0, 0),
                                 (board.x + j*BOX_SIZE, board.y + i*BOX_SIZE),
                                 (board.x + (j+1)*BOX_SIZE, board.y + (i+1)*BOX_SIZE), 1)
                pygame.draw.line(WIN, (255, 0, 0),
                                 (board.x + (j+1)*BOX_SIZE, board.y + i*BOX_SIZE),
                                 (board.x + j*BOX_SIZE, board.y + (i+1)*BOX_SIZE), 1)
    # pygame.display.update()

def drawPieces(board):
    colors = {
        "blue": (0, 0, 255),
        "green": (0, 255, 0),
        "red": (255, 0, 0),
        "yellow": (255, 255, 0)
    }

    positions = {
        "blue":   (0, 2),
        "green":  (4, 2),
        "red":    (2, 0),
        "yellow": (2, 4)
    }

    # Offsets to place 4 pieces inside one box (mini 2x2 grid)
    offsets = [(29,29), (69,29), (29,69), (69,69)]

    for group, (row, col) in positions.items():
        base_x = board.x + col * BOX_SIZE
        base_y = board.y + row * BOX_SIZE
        for i in range(4):
            dx, dy = offsets[i]
            pygame.draw.circle(WIN, colors[group],
                               (base_x + dx, base_y + dy),
                               BOX_SIZE // 5)

def main():
    run = True
    board = pygame.Rect(150, 50, BOX_SIZE*5, BOX_SIZE*5)
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawBoard(board)
        drawPieces(board)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    
if __name__ == "__main__":
    main()
    