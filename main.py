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

    #Drawing
    screen.fill(BLACK) #Refresh screen
    mouse_pos = pygame.mouse.get_pos()
    bound.draw(screen,WHITE)
    
    
    ray = Ray(10,250,mouse_pos[0],mouse_pos[1])

    #Denominator
    den = (bound.x1 - bound.x2) * (250 - mouse_pos[1]) - (bound.y1 - bound.y2) * (10 - mouse_pos[0])
    if den != 0:
        u = ((bound.x1 - 10) * (bound.y1 - bound.y2) - (bound.y1 - 250) * (bound.x1 - bound.x2))/den
        t = ((bound.x1 - 10) * (250 - mouse_pos[1]) - (bound.y1 - 250) * (10 - mouse_pos[0]))/den

    if t >= 0 and t<=1:
        if u >= 0 and u <= 1:
            point = (bound.x1 + t*(bound.x2 - bound.x1), bound.y1 + t*(bound.y2 - bound.y1))
            pygame.draw.circle(screen, RED, point,4)
            ray.x2 = point[0]
            ray.y2 = point[1]
            ray.draw(screen,WHITE) 
        else:
            ray.draw(screen,WHITE) 
    else: ray.draw(screen,WHITE)
       

    pygame.display.flip()
    pygame.display.update()