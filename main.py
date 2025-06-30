# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.Clock.tick(60)
        
    dt = pygame.time.Clock().tick(60) / 1000



    

if __name__ == "__main__":
    main()
