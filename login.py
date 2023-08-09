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
font = pygame.font.SysFont("arial", 25)
smallfont = pygame.font.SysFont("arial", 15)
slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)

# Load Images
Space = pygame.image.load("space_start.jpg")

# Function to create a button
def create_button(msg, x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            first_level()
    else:
        pygame.draw.rect(screen,defaultcolor, (x, y, width, height))
    # Start button text
    startbuttontext = smallfont.render(msg, True, blackish)
    screen.blit(startbuttontext, (int(890 + (width / 2)), int(y + (y / 2))))
    
# Start menu returns true until we click the start button
def start_menu():
    startText = font.render("The Space Game", True, slategrey)
    
