import sys
import pygame

# Initializing
pygame.init()

# Set Clock
clock = pygame.time.Clock()

# Create Screen
screen_width = 400
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Game")

# Initialize constants
font = pygame.font.SysFont("arial", 40)
smallfont = pygame.font.SysFont("arial", 15)
slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)

# Load Images
space = pygame.image.load("space_start.jpg")


# Function to create a button
def create_button(msg, x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            login()
    else:
        pygame.draw.rect(screen,defaultcolor, (x, y, width, height))
    # Start button text
    startbuttontext = font.render(msg, True, blackish)
    screen.blit(startbuttontext, (int(150), int(470)))
    
# Start menu returns true until we click the start button
def start_menu():
    startText = font.render("Space Game", True, (slategrey))
    
    while True:
        screen.fill((0, 0, 0))
        
        # Displays the board room picture
        screen.blit(pygame.transform.scale(space, (550,700)), (0,0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 20))
        # start button (left, top, width, height)
        create_button("LOGIN", 100, 450, 200, 80, lightgrey, slategrey)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(60)
        return True
    
def login():
    startText = font.render("WELCOME", True, slategrey)
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(60)
        

# Game Loop
while True:
    
    start_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
    
