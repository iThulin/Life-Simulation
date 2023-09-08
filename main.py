import pygame
from pygame.locals import *

pygame.init()

# Defining colors to be used in the display
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    CANVAS = pygame.display.set_mode((500, 500))
    FramePerSec = pygame.time.Clock()
    FPS = 60

    # Initial conditions
    CANVAS.fill(WHITE)
    pygame.display.set_caption("Game")

    # Game loop begins
    while True: 
        # code goes here




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        pygame.display.update() 
        FramePerSec.tick(FPS)


main()