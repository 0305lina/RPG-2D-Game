import pygame
from sys import exit

# Initiates all the function related to pygame
pygame.init()
# Display surface of the screen (width, height)
screen = pygame.display.set_mode((800, 400))
# Update title of the surface
pygame.display.set_caption('RPG 2D Academic Game')
# Control frame break
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Background
sky_surf = pygame.image.load('graphic/sky.png').convert()
sky_surf = pygame.transform.scale(sky_surf, (800, 280))
ground_surf = pygame.image.load('graphic/ground.png').convert()

score_surf = test_font.render('Start the Game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

#Character
snoopy_surf = pygame.image.load('graphic/snoopy.png').convert_alpha()
snoopy_surf = pygame.transform.scale(snoopy_surf, (100, 80))
snoopy_x_pos = 0
snoopy_rect = snoopy_surf.get_rect(midbottom = (50, 280))
snoopy_grav = 0

cat_surf = pygame.image.load('graphic/cat.png')
cat_surf = pygame.transform.scale(cat_surf, (100, 80))
cat_rect = cat_surf.get_rect(bottomright = (750, 280))


# This game will run forever in this loop
while True:
    for event in pygame.event.get():
        # pygame.QUIT is x button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Button press -> check collision is more efficient
        if event.type == pygame.MOUSEBUTTONDOWN and snoopy_rect.bottom >= 280:
            if snoopy_rect.collidepoint(event.pos):
                snoopy_grav = -20

        # Only allow jump when the player is on the ground
        if event.type == pygame.KEYDOWN and snoopy_rect.bottom >= 280:
            if event.key == pygame.K_SPACE:
                snoopy_grav = -20
        

    #block image transfer (one surface on another surface)
    screen.blit(ground_surf, (-10,120))
    screen.blit(sky_surf, (0,0))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 50)
    screen.blit(score_surf, score_rect)
    cat_rect.x -= 3
    if cat_rect.right <= 0:
        cat_rect.left = 800
    screen.blit(cat_surf,cat_rect)
    snoopy_rect.left += 1

    # Player
    snoopy_grav += 1
    snoopy_rect.y += snoopy_grav
    if snoopy_rect.bottom >= 280:
        snoopy_rect.bottom = 280
    screen.blit(snoopy_surf, snoopy_rect)

    #draw all our elements
    #update everything
    pygame.display.update() 
    clock.tick(60) #ceiling == Frame Rate