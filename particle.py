import random

class Particle:
    def __init__(self, color, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randint(0, x_boundary)
        self.y = random.randint(0, y_boundary)
        self.vel_x = random.uniform(-1, 1)
        self.vel_y = random.uniform(-1, 1)
        self.color = color
        self.size = random.randint(0, 10)

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x <= 0 + self.size:
            self.vel_x = -self.vel_x
        if self.x >= self.x_boundary - self.size:
            self.vel_x = -self.vel_x
        if self.y <= 0 + self.size:
            self.vel_y = -self.vel_y
        if self.y >= self.y_boundary - self.size:
            self.vel_y = -self.vel_y