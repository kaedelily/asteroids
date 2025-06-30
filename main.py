# this allows us to use code from
# the open-source pygame library
# throughout this file
import constants
import pygame
import player 

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    player1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player1.draw(screen)
        pygame.display.flip()
        tick = clock.tick(60)
        
        dt = tick / 1000.0
    

if __name__ == "__main__":
    main()
