import random

class Particle:
    def __init__(self, color, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randint(0, x_boundary)
        self.y = random.randint(0, y_boundary)
        self.vel_x = random.uniform(-0.001, 0.001)
        self.vel_y = random.uniform(-0.001, 0.001)
        self.accel_x = random.uniform(-0.00001, 0.00001)
        self.accel_y = random.uniform(-0.00001, 0.00001)
        self.color = color
        self.size = random.randint(0, 10)

    def move(self):

        # self.dt is one time step in the movement function.
        self.vel_x += self.accel_x #* self.dt
        self.vel_y += self.accel_y #* self.dt
        self.x += self.x * self.vel_x
        self.y += self.y * self.vel_y

        # Handle collisions with the walls of the "box"
        if self.x < 0  or self.x > self.x_boundary - self.size:
            #self.x = -self.x if self.x < 0 else 2 * self.size - self.x
            self.vel_x = -self.vel_x
            #self.accel_x = 0
        if self.y < 0 or self.y > self.y_boundary - self.size:
            #self.y = -self.y if self.y < 0 else 2 * self.size - self.y
            self.vel_y = -self.vel_y
            #self.accel_y = 0
