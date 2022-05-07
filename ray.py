import pygame

class Ray():

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    

    def draw(self,screen,colour):
        pygame.draw.line(screen,colour,(self.x1,self.y1),(self.x2,self.y2))


    def cast(self,bound,screen,colour):
        # Maths from the wikipedia article to determine whether the lines cross and at which point.
        den = (bound.x1 - bound.x2) * (self.y1 - self.y2) - (bound.y1 - bound.y2) * (self.x1 - self.x2)
        if den != 0:
            u = ((bound.x1 - self.x1) * (bound.y1 - bound.y2) - (bound.y1 - self.y1) * (bound.x1 - bound.x2))/den
            t = ((bound.x1 - self.x1) * (self.y1 - self.y2) - (bound.y1 - self.y1) * (self.x1 - self.x2))/den

            if (t >= 0 and t<=1) and (u >= 0 and u <= 1):
                #Point lines cross, drawn by circle and ray cut to that point.
                point = (bound.x1 + t*(bound.x2 - bound.x1), bound.y1 + t*(bound.y2 - bound.y1))
                pygame.draw.circle(screen, colour, point,4)
                self.x2 = point[0]
                self.y2 = point[1]
                self.draw(screen,colour) 
        
            # else:
            #     self.draw(screen,colour)