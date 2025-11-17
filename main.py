import pygame
import time
import random

WIDTH, HEIGHT = 800, 600
BOX_SIZE = 100
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ashta Cheamma")

def drawBoard(board):
    WIN.fill((255, 255, 255))
    pygame.draw.rect(WIN, (255, 0, 0), board, 2)
    cols=5
    rows=5
    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(WIN, (0, 0, 0), (board.x + j*BOX_SIZE, board.y + i*BOX_SIZE, BOX_SIZE, BOX_SIZE), 1)
            if (i,j) in {(0,2),(4,2),(2,0),(2,4),(2,2)}:
                pygame.draw.line(WIN, (255, 0, 0), (board.x + j*BOX_SIZE, board.y + i*BOX_SIZE), (board.x + (j+1)*BOX_SIZE, board.y + (i+1)*BOX_SIZE), 1)
                pygame.draw.line(WIN, (255, 0, 0), (board.x + (j+1)*BOX_SIZE, board.y + i*BOX_SIZE), (board.x + j*BOX_SIZE, board.y + (i+1)*BOX_SIZE), 1)
    pygame.display.update()
    # show this for game over
    #     x = random.randint(0, WIDTH - BOX_SIZE)
    #     y = random.randint(0, HEIGHT - BOX_SIZE)
    #     pygame.draw.rect(WIN, (0, 0, 0), (x, y, BOX_SIZE, BOX_SIZE), 2)

def main():
    run = True
    board = pygame.Rect(150, 50, BOX_SIZE*5, BOX_SIZE*5)
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawBoard(board)
    pygame.quit()
    
if __name__ == "__main__":
    main()