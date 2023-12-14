import pygame
import math
import random

class AdvancedCreature:

    def __init__(self,
                 metabolism, 
                 size,
                 move_speed,
                 color,
                 x_boundary, 
                 y_boundary):
        
        self.parts = []
        self.metabolism = metabolism
        self.size = size
        self.area = math.pi * (self.size ** 2)
        self.move_speed = move_speed # [x, y, r] = (cardinal, lateral, rotation)
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, x_boundary)
        self.y = random.randrange(0, y_boundary)

    def __repr__(self):
        return 'Creature({},{}.({},{}))'.format(self.color,
                                                self.size,
                                                self.x,
                                                self.y)
    
    def __str__(self):
        return "Color: {} creature object of size {}. Located at {},{}".format(self.color,
                                                                              self.size,
                                                                              self.x,
                                                                              self.y)

    def move(self):
        # This block can be used to manually control the player creature
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.move_speed[1]
        if keys[pygame.K_RIGHT]:
            self.x += self.move_speed[1]
        if keys[pygame.K_UP]:
            self.y += self.move_speed[0]
        if keys[pygame.K_DOWN]:
            self.y -= self.move_speed[0]
        

    def check_bounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary

        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary


    def add_part(self, new_part):
        self.parts.append(new_part)