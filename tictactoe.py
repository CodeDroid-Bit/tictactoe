
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
rect1 = pygame.Rect(0, 400, 600, 15)
rect2 = pygame.Rect(0, 175, 600, 15)
rect3 = pygame.Rect(175, 0, 15, 600)
rect4 = pygame.Rect(400, 0, 15, 600)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((255, 255, 255))
	pygame.draw.rect(screen, BLACK, rect1)
	pygame.draw.rect(screen, BLACK, rect2)
	pygame.draw.rect(screen, BLACK, rect3)
	pygame.draw.rect(screen, BLACK, rect4)

	pygame.display.flip()
pygame.quit()
