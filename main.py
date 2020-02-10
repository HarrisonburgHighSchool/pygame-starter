# Before running this program, you must make sure you have installed pygame
# In the terminal, run the following command:
# py -m pip install pygame --user

import pygame # import the game engine
pygame.init() # initialize the engine

# Create the window
win = pygame.display.set_mode((500, 500))

# Set up a loop
run = True
while run:
  
  # Game code starts here ---------------------------------------
    
  # Draw a rectangle
  pygame.draw.rect(win, (255, 0, 0), (50, 50, 50, 50))
  
  #Update the display
  pygame.display.update()
pygame.quit()
