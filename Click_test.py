import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Button Test")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for MOUSEBUTTONDOWN event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(f"Left button clicked at position: {event.pos}")
            elif event.button == 2:
                print(f"Middle button (scroll wheel) clicked at position: {event.pos}")
            elif event.button == 3:
                print(f"Right button clicked at position: {event.pos}")
            elif event.button == 4:
                print("Mouse wheel scrolled up")
            elif event.button == 5:
                print("Mouse wheel scrolled down")

    # Drawing
    screen.fill(BLACK)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()