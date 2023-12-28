import random
import math
import decimal as dec

class Particle:
    def __init__(self, color, init_x, init_y, x_boundary, y_boundary, charge):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = dec.Decimal(random.uniform(0, x_boundary))
        self.y = dec.Decimal(random.uniform(0, y_boundary))
        self.vel_x = dec.Decimal(0)
        self.vel_y = dec.Decimal(0)
        self.accel_x = dec.Decimal(0)
        self.accel_y = dec.Decimal(0)
        self.color = color
        self.size = random.randint(1, 5)
        self.mass = dec.Decimal(self.size).sqrt()
        self.charge = charge

    def move(self):

        # self.dt is one time step in the movement function.
        self.vel_x += self.accel_x 
        self.vel_y += self.accel_y 
        self.x += dec.Decimal(self.x) * dec.Decimal(self.vel_x)
        self.y += dec.Decimal(self.y) * dec.Decimal(self.vel_y)

        # Handle collisions with the walls of the "box"
        if self.x < 0 + self.size:
            self.vel_x = -self.vel_x
            #self.accel_x = 0
        if self.x > self.x_boundary - self.size:
            self.vel_x = -self.vel_x
        if self.y < 0 + self.size:
            self.vel_y = -self.vel_y
            #self.accel_y = 0
        if self.y > self.y_boundary - self.size:
            self.vel_y = -self.vel_y

    def calculate_force(self, other_x, other_y, other_charge):
        dist_x = self.x - other_x
        dist_y = self.y - other_y

        # If particles are at the same point return no force
        if dist_x == dist_y == 0:
            return 0, 0, 0 # No force in this case

        # If particles are too far apart break the calculation
        if dist_x + dist_y > 400:
            return 0, 0, 0

        # Force = k * q1 * q2 / r_sq
        k = dec.Decimal(8.99e9)
        q_1 = self.charge
        q_2 = other_charge
        r_sq = dec.Decimal(dist_x ** 2 + dist_y ** 2).sqrt()

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

        #print(f"Accel_x: {self.accel_x}")
        #print(f"Accel_y: {self.accel_y}")
        