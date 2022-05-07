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

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Drawing screen and boundary
    screen.fill(BLACK)
    mouse_pos = pygame.mouse.get_pos()
    for bound in boundaries:
        bound.draw(screen,WHITE)
    
    light = Lightsource(mouse_pos[0],mouse_pos[1],WIDTH,HEIGHT)
    light.illuminate()

    for ray in light.rays:
        closest_bound = boundaries[0]
        for bound in boundaries:
            pass
            
        ray.cast(bound,screen,WHITE)


    #update screen
    pygame.display.flip()