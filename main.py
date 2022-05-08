"""
George Brignell-Cash
Ray-Tracer in Python

links:
https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
"""
#imports
import pygame
from boundary import Boundary
from ray import Ray
from lightsource import Lightsource
import math
import random


#Initalise game
pygame.init()

#Constants
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
WIDTH = 1000
HEIGHT = 1000

#Creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption('2D RayTracer')

#Boundary/s and ray/s
boundaries = []
boundaries.append(Boundary(400,100,400,400))
for i in range(3):
    bound = Boundary(random.randrange(0,WIDTH),random.randrange(0,HEIGHT),random.randrange(0,WIDTH),random.randrange(0,HEIGHT))
    boundaries.append(bound)


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