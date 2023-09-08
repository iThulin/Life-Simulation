import pygame
from pygame.locals import *
from creature import Creature

pygame.init()

# Defining colors to be used in the display
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1000
HEIGHT = 1000
FPS = 60

# Starting Creature parameters
STARTING_BLUE_CREATURES = 10
STARTING_RED_CREATURES = 10

# Initialize the game environment
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life Simulator")

clock = pygame.time.Clock()

def draw_environment(creature_list):
    display.fill(WHITE)

    for creature_dict in creature_list:
        for creature_id in creature_dict:
            creature = creature_dict[creature_id]
            pygame.draw.circle(display, creature.color, [creature.x, creature.y], creature.size)
            creature.move()

    pygame.display.update()

def main():
    blue_creatures = dict(enumerate([Creature(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_CREATURES)]))
    red_creatures = dict(enumerate([Creature(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_CREATURES)]))

    # Game loop begins
    while True: 
        # code goes here




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        #pygame.display.update() 

        draw_environment([blue_creatures, red_creatures])
        clock.tick(FPS)

if __name__ == '__main__':
    main()