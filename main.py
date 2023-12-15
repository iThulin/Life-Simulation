import pygame
from pygame.locals import *
import numpy as np
import logging
import math
from creature import Creature
from Advanced_creature import AdvancedCreature

'''
DEBUG   Detailed information, typically of interest only when diagnosing problems.
INFO    Confirmation that things are working as expected.
WARNING An indication that something unexpected happened, or indicative of some problem in the near future
ERROR   Due to a more serious problem, the software has nt been able to perform some function
CRITICAL    A serious error, indicating that the program itself may be unable to continue running.
'''

logging.basicConfig(filename='logfile.log', level=logging.INFO)

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

# Define Creature parameters
STARTING_BLUE_CREATURES = 10
STARTING_RED_CREATURES = 10
STARTING_GREEN_CREATURES = 10
STARTING_ADV_CREATURES = 10

# Initialize the game environment
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life Simulator")

clock = pygame.time.Clock()

# OBJECTS

class BlueCreature(Creature):
    def __init__(self, x_boundary, y_boundary):
        Creature.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__ (self, other_creature):
        logging.info('Creature add op: {}'.format(str(self.color), str(other_creature.color)))
        if other_creature.color == (255, 0, 0):
            self.size -= other_creature.size
            other_creature.size -= self.size

        elif other_creature.color == (0, 255, 0):
            self.size += other_creature.size
            other_creature.size = 0

        elif other_creature.color == (0, 0, 255):
            pass
        else:
            raise Exception('Tried to combine one or multiple creatures of unsupported colors!')

class RedCreature(Creature):
    def __init__(self, x_boundary, y_boundary):
        Creature.__init__(self, (255, 0, 0), x_boundary, y_boundary)

class GreenCreature(Creature):
    def __init__(self, x_boundary, y_boundary):
        Creature.__init__(self, (0, 255, 0), x_boundary, y_boundary, movement_range=(-0.01, .01))

class BlackCreature(AdvancedCreature):
    def __init__(self, x_boundary, y_boundary):
        AdvancedCreature.__init__(self,
                                    metabolism= 0,
                                    size= 10,
                                    move_speed= (1, 1, 1),
                                    color= BLACK,
                                    x_boundary= x_boundary,
                                    y_boundary= y_boundary)


def log_creatures(creature_list):
    print(creature_list)
    #for index in range (0, len(creature_list)):
        #print(repr(creature_list[index]))

def is_touching(c1, c2):
    return np.linalg.norm(np.array([c1.x, c1.y])-np.array([c2.x, c2.y])) < (c1.size + c2.size)

def handle_collisions(creature_list):
    log_creatures(creature_list)

    print("\nSTART\n")
    creature_num = 0
    #for species in creature_list:
        #print(f"Species: {species}")


    for creature in creature_list:
        print(f"Creature: {creature_num}, \n{creature}")
        creature_num += 1
        other_creature_num = 0
        for other_creature in creature:
            print(f"Other Creature: {other_creature_num}, {other_creature}")
            other_creature_num += 1
            #logging.debug('Checking if creatures touching {} + {}'.format(str(creature.color), str(other_creature.color)))
            '''
            if is_touching(creature, other_creature):
                # Eat other creature
                if creature.stomach_volume_remaining > other_creature.size:
                    creature.stomach_volume_remaining += other_creature.size
                    del other_creature
            '''

# currently pulling list and no the individual creatures. 

    print("\nEND\n")

    return creature_list

def draw_environment(creature_list):
    display.fill(WHITE)
    handle_collisions(creature_list)
    #log_creatures(creature_list)

    for creature_dict in creature_list:
        for creature_id in creature_dict:
            creature = creature_dict[creature_id]
            pygame.draw.circle(display, creature.color, [creature.x, creature.y], creature.size)
            creature.move()
            creature.check_bounds()    
    
    pygame.display.update()
    return creature_list

def main():
    blue_creatures = dict(enumerate([BlueCreature(WIDTH, HEIGHT) for i in range(STARTING_BLUE_CREATURES)]))
    red_creatures = dict(enumerate([RedCreature(WIDTH, HEIGHT) for i in range(STARTING_RED_CREATURES)]))
    green_creatures = dict(enumerate([GreenCreature(WIDTH, HEIGHT) for i in range(STARTING_GREEN_CREATURES)]))
    black_creatures = dict(enumerate([BlackCreature(WIDTH, HEIGHT) for i in range(STARTING_ADV_CREATURES)]))

    # Game loop begins
    while True: 
        # code goes here
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        pygame.display.update() 

        draw_environment([black_creatures, blue_creatures, red_creatures, green_creatures])
        clock.tick(FPS)

if __name__ == '__main__':
    main()