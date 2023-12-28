import pygame
from pygame.locals import *
import numpy as np
import random
import logging
import math
from particle import Particle
from datetime import datetime
import decimal as dec

'''
DEBUG   Detailed information, typically of interest only when diagnosing problems.
INFO    Confirmation that things are working as expected.
WARNING An indication that something unexpected happened, or indicative of some problem in the near future
ERROR   Due to a more serious problem, the software has not been able to perform some function
CRITICAL    A serious error, indicating that the program itself may be unable to continue running.
'''

LOG_FILENAME = datetime.now().strftime('Logs\logfile_%H_%M_%d.%m.%Y.log')
logging.basicConfig(filename=LOG_FILENAME, filemode='w', level=logging.INFO)

# Define the display parameters
WIDTH = 1000
HEIGHT = 1000
FPS = 30

# Define colors to be used in the display
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define particle parameters
STARTING_PARTICLES = 10
STARTING_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
STARTING_CHARGE = dec.Decimal(1e-8)
SECOND_PARTICLES = 20
SECOND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
SECOND_CHARGE = dec.Decimal(-1e-8)

# Initialize the game environment
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulator")
clock = pygame.time.Clock()

clock = pygame.time.Clock()

# METHODS

def log_objects(particles):
    #print(particles)
    pass

def is_touching(c1, c2):
    return np.linalg.norm(np.array([c1.x, c1.y])-np.array([c2.x, c2.y])) < (c1.size + c2.size)

def handle_collisions(particles):
    log_objects(particles)

    #print("\nSTART\n")

    for particle in particles:
        for second_particle in particles:
            particle.apply_force(second_particle)
            #second_particle.apply_force(particle)

    #print("\nEND\n")

    return particles

def update_sim(particles):
    #handle_collisions(particles)

    for particle in particles:
        for second_particle in particles:
            particle.apply_force(second_particle)
            particle.move()
            pygame.draw.circle(display, particle.color, (float(particle.x), float(particle.y)), particle.size)

    pygame.display.update()
    clock.tick(FPS)
    return particles

def create_particles(particles, num_particles, color, WIDTH, HEIGHT, CHARGE):
    init_num_x = dec.Decimal(WIDTH / 2)
    init_num_y = dec.Decimal(HEIGHT / 2)

    if len(particles) == 0:
        for _ in range(0, STARTING_PARTICLES):
            init_num_x += dec.Decimal(5)
            init_num_y += dec.Decimal(5)
            particles.append(Particle(color, init_x= init_num_x, init_y= init_num_y, x_boundary=WIDTH, y_boundary=HEIGHT, charge=CHARGE))
        for entity in particles:
            pygame.draw.circle(display, color, (float(entity.x), float(entity.y)), entity.size)
            logging.info('Initial particle %s', entity.color)
    else:
        for _ in range (0, num_particles - len(particles)):
            init_num_x += dec.Decimal(5)
            init_num_y += dec.Decimal(5)
            new_particle = Particle(color, init_x= init_num_x, init_y= init_num_y, x_boundary=WIDTH, y_boundary=HEIGHT, charge=CHARGE)
            particles.append(new_particle)
            pygame.draw.circle(display, new_particle.color, (float(new_particle.x), float(new_particle.y)), new_particle.size)
            logging.info('Added particle %s', new_particle.color)
    return particles


def main():
    # Game loop begins
    running = True
    particle_spawned = False
    second_particle_spawned = False
    particles = []
    while running: 
        display.fill(BLACK)
        # code goes here
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        if particle_spawned == False:
            create_particles(particles,
                            STARTING_PARTICLES,
                            color=STARTING_COLOR,
                            WIDTH=WIDTH,
                            HEIGHT=HEIGHT,
                            CHARGE= STARTING_CHARGE)
            particle_spawned = True
        if second_particle_spawned == False:
            create_particles(particles,
                             SECOND_PARTICLES,
                             color=SECOND_COLOR,
                             WIDTH= WIDTH,
                             HEIGHT= HEIGHT,
                             CHARGE= SECOND_CHARGE)
            second_particle_spawned = True

        
        update_sim(particles)

if __name__ == '__main__':
    main()