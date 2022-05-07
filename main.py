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
import math

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
    

    rays = []
    #Create and draw ray
    view_size = math.sqrt(WIDTH**2+HEIGHT**2)
    for angle in range(0,360,5):
        rad = angle * math.pi / 180
        ray_ = Ray(mouse_pos[0],mouse_pos[1],mouse_pos[0] + view_size*math.cos(rad), mouse_pos[1] + view_size*math.sin(rad))
        rays.append(ray_)

    for ray in rays:
        ray.cast(bound,screen,WHITE)


    #update screen
    pygame.display.flip()