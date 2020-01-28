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
  pygame.time.delay(1000/60) # Loop the code 60 times per second
  
  # Draw a rectangle
  pygame.draw.rect(win, (255, 0, 0), (50, 50, 50, 50))
  
pygame.quit()
