# my fire pygame file
import pygame

# define some colors
# upper case variables show that they are global 
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
# DARK_BLUE=(18,100,128)

# initializes the game
pygame.init()

# set the width and height of the screen [width,height]
screen_size=(700,700)
screen= pygame.display.set_mode(screen_size)

pygame.display.set_caption("My First Game!")

# keep a varuable done that keeps track of if I am still playing 
done=False

clock=pygame.time.Clock() # used to manage how fast the screen update

# this is the game loop
while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
	screen.fill(BLUE)
	clock.tick(60)
	pygame.draw.line(screen,BLUE, (100, 350), (300,350))

# Game logic should go here

# screen-clearing code goes here

# here, we clear the screen to white. don't put other drawing commads
# above this, or they will be erased woith this command

# if you want a background image, replace this clear wiuth blit'ing the background image 

#limit to 60 frams per minute

pygame.quit()















