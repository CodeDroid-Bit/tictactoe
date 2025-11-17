
import pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# x, y, width, height
line1 = pygame.Rect(0, SCREEN_HEIGHT/3, SCREEN_HEIGHT, 15) #top sideways
line2 = pygame.Rect(0, SCREEN_HEIGHT/3*2, SCREEN_HEIGHT, 15) #bottom sideways
line3 = pygame.Rect(SCREEN_HEIGHT/3, 0, 15, SCREEN_HEIGHT) #
line4 = pygame.Rect(SCREEN_HEIGHT/3*2, 0, 15, SCREEN_HEIGHT)
Shape_x = pygame.rect()

def tictactoe_board(line1,line2,line3,line4):
    pygame.draw.rect(screen, BLACK, line1)
    pygame.draw.rect(screen, BLACK, line2)
    pygame.draw.rect(screen, BLACK, line3)
    pygame.draw.rect(screen, BLACK, line4)
    return


screen.fill((255, 255, 255))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if area_1.collidepoint(mouse_pos):
                pygame.draw.rect(screen, BLACK, Shape_x)

    tictactoe_board(line1,line2,line3,line4)

    pygame.display.flip()
pygame.quit()
