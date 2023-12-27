import random
import math

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
        self.mass = math.sqrt(self.size)
        self.charge = 1

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

    def calculate_force(self, other_x, other_y, other_charge):
        dist_x = self.x - other_x
        dist_y = self.y - other_y

        # If particles are at the same point return no force
        if dist_x == dist_y == 0:
            return 0, 0, 0 # No force in this case

        # Force = k * q1 * q2 / r_sq
        k = 8.99e9
        q_1 = self.charge
        q_2 = other_charge
        r_sq = math.sqrt(dist_x ** 2 + dist_y ** 2)

        # Calculate the force magnitude
        F = (k * q_1 * q_2) / r_sq

        # Calculate the force components along the x and y axes
        force_x = F * (dist_x / r_sq)
        force_y = F * (dist_y / r_sq)

        # Determine direction of force
        if (q_1 > 0 and q_2 > 0) or (q_1 < 0 and q_2 < 0):
            force_x *= -1
            force_y *+ -1

        return force_x, force_y, F # Return for components and magnitude
    
    def apply_force(self, other):
        new_force = self.calculate_force(other.x, other.y, other.charge)

        self.accel_x += new_force[0] / self.mass
        self.accel_y += new_force[1] / self.mass
        