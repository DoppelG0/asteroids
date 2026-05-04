import pygame
import circleshape
import constants
from logger import log_event
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius,constants.LINE_WIDTH)
    
    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        degree = random.uniform(20,50)
        new_asteroid1_vector = self.velocity.rotate(degree)
        new_asteroid2_vector = self.velocity.rotate(-degree)
        smaller_asteroids = self.radius - constants.ASTEROID_MIN_RADIUS
        smaller_asteroid1 = Asteroid(self.position[0],self.position[1],smaller_asteroids)
        smaller_asteroid1.velocity = new_asteroid1_vector * 1.2
        smaller_asteroid2 = Asteroid(self.position[0],self.position[1],smaller_asteroids)
        smaller_asteroid2.velocity = new_asteroid2_vector * 1.2
