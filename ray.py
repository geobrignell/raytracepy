import pygame

class Ray():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def draw(self,screen,colour):
        pygame.draw.line(screen,colour,(self.x1,self.y1),(self.x2,self.y2))