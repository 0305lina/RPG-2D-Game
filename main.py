import pygame
from sys import exit

# Initiates all the function related to pygame
pygame.init()
# Display surface of the screen (width, height)
screen = pygame.display.set_mode((1200, 800))
# Update title of the surface
pygame.display.set_caption('RPG 2D Academic Game')
# Control frame break
clock = pygame.time.Clock()


# 33.31
test_surf = pygame.Surface((100, 200))
test_surf.fill('Red')

# This game will run forever in this loop
while True:
    for event in pygame.event.get():
        # pygame.QUIT is x button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #block image transfer (one surface on another surface)
    screen.blit(test_surf, (0,0))

    #draw all our elements
    #update everything
    pygame.display.update() 
    clock.tick(60) #ceiling 