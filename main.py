"""
George Brignell-Cash
Ray-Tracer in Python

links:
https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
"""
import pygame
from boundary import Boundary
from ray import Ray

pygame.init()

#Constants
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
WIDTH = 600
HEIGHT = 600

#Creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption('2D RayTracer')

#Boundary
bound = Boundary(400,100,400,400)


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
    bound.draw(screen,WHITE)
    
    #Create and draw ray
    ray = Ray(10,250,mouse_pos[0],mouse_pos[1])
    ray.cast(bound,screen,WHITE)

    pygame.display.flip()