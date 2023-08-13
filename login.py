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
midfont = pygame.font.SysFont("arial", 25)
slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)
white = (255, 255, 255)
black = (0, 0, 0)

# Load Images
space = pygame.image.load("space_start.jpg")


# Function to create a button
def create_button( x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen,defaultcolor, (x, y, width, height))
    
# Start menu returns true until we click the start button
def start_menu():
    startText = font.render("Space Game", True, (slategrey))
    
    while True:
        screen.fill((0, 0, 0))
        
        # Displays the board room picture
        screen.blit(pygame.transform.scale(space, (550,700)), (0,0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 20))
        # start button (left, top, width, height)
        start_button = create_button(100, 450, 200, 80, lightgrey, slategrey)
        
        if start_button:
            login()
            
        startbuttontext = font.render("LOGIN", True, blackish)
        screen.blit(startbuttontext, (150, 470))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(60)
        return True
    
def login():
    startText = font.render("WELCOME", True, slategrey)
    newText = font.render("NEW USER",True, blackish)
    returnText = font.render("Returner", True, blackish)
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 20))
        
        # button (left, top, width, height)
        newButton = create_button((screen_width / 2) - 100, int(screen_height * .33), 200, 50, lightgrey, slategrey)
        
        if newButton:
            new_game()
            
        screen.blit(newText, ((screen_width / 2) - (newText.get_width() / 2), int(screen_height * .33)))
        
        returnButton = create_button((screen_width / 2) - 100, screen_height / 2, 200, 50, lightgrey, slategrey)
        
        if returnButton:
            print("Return Button is clicked.")
        
        screen.blit(returnText, ((screen_width / 2) - (returnText.get_width() / 2), screen_height / 2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(60)
        
def new_game():
    startText = font.render("Space Game", True, slategrey)
    newUserName = ""
    
    # Make the text grey and white when active
    nameActive = False
    ship1Active = False
    ship2Active = False
    ship3Active = False
    
    # Declare Variables
    characterChoicePrompt = midfont.render ("Choose Your Spacechip", True, slategrey)
    ship1 = pygame.image.load("ship1.jpg")
    ship2 = pygame.image.load("ship2.jpg")
    ship3 = pygame.image.load("ship3.jpg")
    newShip1 = pygame.transform.scale(ship1, (100,100))
    newShip2 = pygame.transform.scale(ship2, (100,100))
    newShip3 = pygame.transform.scale(ship3, (100,100))
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 20))
        
        # Create the text box
        userNameSurface = midfont.render(newUserName, True, white)
        
        # Create the border around the text box with .rect
        # left, top, width, height
        userNameBorder = pygame.Rect(((screen_width - userNameSurface.get_width()) / 2) - 10, screen_height * .15, userNameSurface.get_width() + 10, 50)
        
        # Text surface when user types in
        screen.blit(userNameSurface, ((screen_width - userNameSurface.get_width()) / 2, screen_height * .16))
        
        # Border around character.jpg
        ship1Border = pygame.Rect((screen_width * .045) - 4, (screen_height * .55) - 4, newShip1.get_width() + 8, newShip1.get_height() + 8)
        ship2Border = pygame.Rect(screen_width * .385 - 4, (screen_height * .55) - 4, newShip2.get_width() + 8, newShip2.get_height() + 8)
        ship3Border = pygame.Rect(screen_width * .7 - 4, (screen_height * .55) - 4, newShip3.get_width() + 8, newShip3.get_height() + 8)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # Mouse and Keyboard
            if event.type == pygame.MOUSEBUTTONDOWN:
                if userNameBorder.collidepoint(event.pos):
                    nameActive = True
                elif ship1Border.collidepoint(event.pos):
                    ship1Active = True
                elif ship2Border.collidepoint(event.pos):
                    ship2Active = True
                elif ship3Border.collidepoint(event.pos):
                    ship3Active = True
                else:
                    nameActive = False
                    ship1Active = False
                    ship2Active = False
                    ship3Active = False
                    
            if event.type == pygame.KEYDOWN:
                if nameActive:
                    if event.key == pygame.K_BACKSPACE:
                        newUserName = newUserName[:-1]
                    else:
                        newUserName += event.unicode
        
        # Handles the click events by switching from white, slategrey, and black
        if nameActive:
            pygame.draw.rect(screen, white, userNameBorder, 2)
            userNamePrompt = midfont.render("Enter Your New Game ID", True, white)
        else:
            pygame.draw.rect(screen, slategrey, userNameBorder, 2)
            userNamePrompt = midfont.render("Enter Your New Game ID", True, white)
            
        if ship1Active:
            ship1name = smallfont.render("X-18 Argonaut", True, white)
            pygame.draw.rect(screen, white, ship1Border, 2)
            ship2Active = False
            ship3Active = False
        else: 
            ship1name = smallfont.render("X-18 Argonaut", True, slategrey)
            pygame.draw.rect(screen, black, ship1Border, 2)
            
        
        if ship2Active:
            ship2name = smallfont.render("ISS Ravana", True, white)
            pygame.draw.rect(screen, white, ship2Border, 2)
            ship1Active = False
            ship3Active = False
        else: 
            ship2name = smallfont.render("ISS Ravana", True, slategrey)
            pygame.draw.rect(screen, black, ship2Border, 2)
        
        if ship3Active:
            ship3name = smallfont.render("Infinity Nexus", True, white)
            pygame.draw.rect(screen, white, ship3Border, 2)
            ship2Active = False
            ship1Active = False
        else: 
            ship3name = smallfont.render("Infinity Nexus", True, slategrey)
            pygame.draw.rect(screen, black, ship3Border, 2)
        
        screen.blit(userNamePrompt, ((screen_width - userNamePrompt.get_width()) / 2, (screen_height * .20) + userNameSurface.get_height()))
        screen.blit(characterChoicePrompt, ((screen_width - characterChoicePrompt.get_width()) / 2, screen_height * .45))
        
        #Choose your Character Pictures
        screen.blit(pygame.transform.scale(ship1, (100,100)), (screen_width * .045, screen_height * .55))
        # screen.blit(ship1, (screen_width * .075, screen_height * .45))
        screen.blit(ship1name, ((screen_width + ship1name.get_width()) * .075, screen_height * .80))
        
        screen.blit(pygame.transform.scale(ship2, (100,100)), (screen_width * .385, screen_height * .55))
        # screen.blit(ship2, ((screen_width - ship2.get_width()) / 2, screen_height * .45))
        screen.blit(ship2name, ((screen_width - ship2name.get_width()) / 2, screen_height * .80))
        
        screen.blit(pygame.transform.scale(ship3, (100,100)), (screen_width * .7, screen_height * .55))
        # screen.blit(ship3, ((screen_width - ship3.get_width()) * .9, screen_height * .45))
        screen.blit(ship3name, ((screen_width + ship3name.get_width()) * .6, screen_height * .80))
                
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
    
