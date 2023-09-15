import pygame
from pygame.locals import *

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Platformer')

# Create the player
player = pygame.Rect(50, 50, 40, 60)
player_color = WHITE

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[K_RIGHT]:
        player.x += PLAYER_SPEED

    # Update game logic here (e.g., collision detection, gravity)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the player
    pygame.draw.rect(screen, player_color, player)

    # Update the screen
    pygame.display.update()

pygame.quit()
