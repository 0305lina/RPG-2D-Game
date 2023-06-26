import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RPG Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

def start_page():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if start_button.collidepoint(mouse_pos):
                    next_page()
                elif end_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Clear the screen
        screen.fill(WHITE)
        
        # Draw the start button
        start_button = pygame.Rect(300, 200, 200, 50)
        pygame.draw.rect(screen, BLACK, start_button)
        start_text = font.render("Start", True, WHITE)
        start_text_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_text_rect)
        
        # Draw the end button
        end_button = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(screen, BLACK, end_button)
        end_text = font.render("End", True, WHITE)
        end_text_rect = end_text.get_rect(center=end_button.center)
        screen.blit(end_text, end_text_rect)
        
        # Update the display
        pygame.display.flip()

def next_page():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if level_button.collidepoint(mouse_pos):
                    # Level button clicked, go to level selection page
                    # Add your code for transitioning to the level selection page here
                    level_page()
                elif customize_button.collidepoint(mouse_pos):
                    # Customize button clicked, go to customization page
                    # Add your code for transitioning to the customization page here
                    next_page()

        # Clear the screen
        screen.fill(WHITE)
        
        # Draw the level button
        level_button = pygame.Rect(300, 200, 200, 50)
        pygame.draw.rect(screen, BLACK, level_button)
        level_text = font.render("Level", True, WHITE)
        level_text_rect = level_text.get_rect(center=level_button.center)
        screen.blit(level_text, level_text_rect)
        
        # Draw the customize button
        customize_button = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(screen, BLACK, customize_button)
        customize_text = font.render("Customize", True, WHITE)
        customize_text_rect = customize_text.get_rect(center=customize_button.center)
        screen.blit(customize_text, customize_text_rect)
        
        # Update the display
        pygame.display.flip()

def level_page():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if  hard_button.collidepoint(mouse_pos):
                    next_page()
                elif normal_button.collidepoint(mouse_pos):
                    next_page()
                elif easy_button.collidepoint(mouse_pos):
                    next_page()
        # Clear the screen
        screen.fill(WHITE)
        
        # Draw the hard button
        hard_button = pygame.Rect(300, 200, 200, 50)
        pygame.draw.rect(screen, BLACK, hard_button)
        hard_text = font.render("HARD", True, WHITE)
        hard_text_rect = hard_text.get_rect(center=hard_button.center)
        screen.blit(hard_text, hard_text_rect)
        
        # Draw the normal button
        normal_button = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(screen, BLACK, normal_button)
        normal_text = font.render("NORMAL", True, WHITE)
        normal_text_rect = normal_text.get_rect(center=normal_button.center)
        screen.blit(normal_text, normal_text_rect)

        # Draw the easy button
        easy_button = pygame.Rect(300, 400, 200, 50)
        pygame.draw.rect(screen, BLACK, easy_button)
        easy_text = font.render("EASY", True, WHITE)
        easy_text_rect = easy_text.get_rect(center=easy_button.center)
        screen.blit(easy_text, easy_text_rect)
        
        # Update the display
        pygame.display.flip()

    
# Call the start_page function to display the start page
start_page()
