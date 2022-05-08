import math
from ray import Ray 

class Lightsource():
    def __init__(self,x,y,WIDTH,HEIGHT):
        self.x = x
        self.y = y
        self.rays = []
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def illuminate(self):#Creates rays around the point
        view_size = math.sqrt(self.WIDTH**2+self.HEIGHT**2)

        for angle in range(0,360,5):
            rad = angle * math.pi / 180

            ray_ = Ray(self.x,self.y, self.x + view_size*math.cos(rad), self.y + view_size*math.sin(rad))
            self.rays.append(ray_)
    
        
