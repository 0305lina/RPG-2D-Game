import pygame
import shelve
from sys import exit

# Shelve save and load data
SAVE_DATA = shelve.open("Save User Data")

# Start menu has two buttons: New user, Returned users
# new user: Let user input their name & press the level test button => name is saved and user is lead level test screen
# old user: let user input their name and submit => Welcome the user with the best score and let them re-do the game. 
# if the new score is higher than the old score, replace the old score with new best score

slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)

# Function to create a button
def create_button(x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))

def display_score():
    
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def start_menu():
    start_text = test_font.render("WELCOME TO RPG 2D ACADEMIC GAME", True, (64, 64, 64))
    start_rect = start_text.get_rect(center = (400, 50))
    new_text = test_font.render("New User", True, blackish)
    old_text = test_font.render("Load User", True, blackish)

    while True:
        screen.fill((94, 129, 162))
        screen.blit(start_text, start_rect)
        newUserButton = create_button((screen_width / 2) - 100, int(screen_height * .33), 200, 50, lightgrey, slategrey)

        if newUserButton:
            new_game()
        screen.blit(new_text, ((screen_width / 2) - (new_text.get_width() / 2), int(screen_height * .33)))

        oldUserButtton = create_button((screen_width / 2) - 100, screen_height / 2, 200, 50, lightgrey, slategrey)

        if oldUserButtton:
            load_screen()

        # Load CEO button text
        screen.blit(old_text, ((screen_width / 2) - (new_text.get_width() / 2), screen_height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)
        
#def new_game():


# Initiates all the function related to pygame
pygame.init()
# Display surface of the screen (width, height)
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
# Update title of the surface
pygame.display.set_caption('RPG 2D Academic Game')
# Control frame break
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# Background
sky_surf = pygame.image.load('graphic/sky.png').convert()
sky_surf = pygame.transform.scale(sky_surf, (800, 280))
ground_surf = pygame.image.load('graphic/ground.png').convert()

# score_surf = test_font.render('Start the Game', False, (64, 64, 64))
# score_rect = score_surf.get_rect(center = (400, 50))

# Enemy
cat_surf = pygame.image.load('graphic/cat.png')
cat_surf = pygame.transform.scale(cat_surf, (60, 40))
cat_rect = cat_surf.get_rect(bottomright = (750, 280))

# Player
snoopy_surf = pygame.image.load('graphic/snoopy.png').convert_alpha()
snoopy_surf = pygame.transform.scale(snoopy_surf, (80, 60))
snoopy_x_pos = 0
snoopy_rect = snoopy_surf.get_rect(midbottom = (50, 280))
snoopy_grav = 0


#New game screen for new user


#Load game screen for existing user


#Redo Screen
snoopy_stand = pygame.image.load('graphic/snoopy_stand.png').convert_alpha()
snoopy_stand_rect = snoopy_stand.get_rect(center = (400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 60))

game_msg = test_font.render('Press space to run again', False, (111, 196, 169))
game_msg_rect = game_msg.get_rect(center = (400, 340))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

# This game will run forever in this loop
while True:
    start_menu()
    for event in pygame.event.get():
        # pygame.QUIT is x button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            # Button press -> check collision is more efficient
            if event.type == pygame.MOUSEBUTTONDOWN and snoopy_rect.bottom >= 280:
                if snoopy_rect.collidepoint(event.pos):
                    snoopy_grav = -22

            # Only allow jump when the player is on the ground
            if event.type == pygame.KEYDOWN and snoopy_rect.bottom >= 280:
                if event.key == pygame.K_SPACE:
                    snoopy_grav = -22
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                cat_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
        
        # if event.type == obstacle_timer and game_active:
        #     print('test')
        
    if game_active:
        #block image transfer (one surface on another surface)
        screen.blit(ground_surf, (-10,120))
        screen.blit(sky_surf, (0,0))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 50)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        cat_rect.x -= 4
        if cat_rect.right <= 0:
            cat_rect.left = 800
        screen.blit(cat_surf,cat_rect)

        # Snoopy moving forward
        # snoopy_rect.left += 1

        # Player
        snoopy_grav += 1
        snoopy_rect.y += snoopy_grav
        if snoopy_rect.bottom >= 280:
            snoopy_rect.bottom = 280
        screen.blit(snoopy_surf, snoopy_rect)

        # collision
        if cat_rect.colliderect(snoopy_rect):
            game_active = False
    #game-over
    else:
        screen.fill((94, 129, 162))
        screen.blit(snoopy_stand, snoopy_stand_rect)

        score_msg = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_msg_rect = score_msg.get_rect(center = (400, 340))
        screen.blit(game_name, game_name_rect)
        
        if score == 0:
            screen.blit(game_msg, game_msg_rect)
        else:
            screen.blit(score_msg, score_msg_rect)

    #draw all our elements
    #update everything
    pygame.display.update() 
    clock.tick(60) #ceiling == Frame Rate