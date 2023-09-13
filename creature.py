import random

class Creature:
    def __init__(self,
                color,
                x_boundary,
                y_boundary,
                size_range=(1, 10),
                movement_range=(-10.0, 10.0)):
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, x_boundary)
        self.y = random.randrange(0, y_boundary)
        self.size = random.uniform(size_range[0], size_range[1])
        self.movement_range = movement_range

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
        self.move_x = random.uniform(self.movement_range[0], self.movement_range[1])
        self.move_y = random.uniform(self.movement_range[0], self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

        # Add a modifier to check bounds before moving?

    def check_bounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary

        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary