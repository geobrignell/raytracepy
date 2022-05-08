"""
George Brignell-Cash
Ray-Tracer in Python

links:
https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection Maths stuff
"""
#imports
import pygame
from boundary import Boundary
from lightsource import Lightsource
import random


#Initalise game
pygame.init()

#Constants
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
WIDTH = 1000
HEIGHT = 1000

#Setting up the game window
pygame.display.set_caption('2D RayTracer') #Name
programIcon = pygame.image.load("icon.png")
pygame.display.set_icon(programIcon) #Setting the icon
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Setting the size
screen.fill(BLACK)

#Setting up bounderies
boundaries = []
boundaries.append(Boundary(400,100,400,400))
for i in range(3):
    bound = Boundary(random.randrange(0,WIDTH),random.randrange(0,HEIGHT),random.randrange(0,WIDTH),random.randrange(0,HEIGHT))
    boundaries.append(bound)
#Added "Walls" around the window
boundaries.append(Boundary(0,0,WIDTH,0))
boundaries.append(Boundary(0,0,0,HEIGHT))
boundaries.append(Boundary(WIDTH,0,WIDTH,HEIGHT))
boundaries.append(Boundary(0,HEIGHT,WIDTH,HEIGHT))


#Game loop
running = True
while running:

    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Getting mouse position
    mouse_pos = pygame.mouse.get_pos()
        
    #Drawing screen and boundary
    screen.fill(BLACK)
    for bound in boundaries:
        bound.draw(screen,WHITE)
    
    #Create the lightsource
    light = Lightsource(mouse_pos[0],mouse_pos[1],WIDTH,HEIGHT)
    light.illuminate()

    #Find closest boundery and draw the line.
    for ray in light.rays:
        closest_bound = ray.closest_bound(boundaries)
        ray.cast(closest_bound,screen,WHITE)

    #update screen
    pygame.display.flip()