# this allows us to use code from
# the open-source pygame library
# throughout this file
import constants
import pygame
import player 
import asteroid
import asteroidfield
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updateable, drawable)
    player1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.PLAYER_RADIUS)
    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updateable, drawable)
    field = pygame.sprite.Group()
    asteroidfield.AsteroidField.containers = (updateable)
    asteroid_field = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        updateable.update(dt)
        for ast in asteroids:
            collision = player1.collision(ast)
            if collision == True:
                print("Game over!")
                sys.exit()
        tick = clock.tick(60)
        dt = tick / 1000.0
    

if __name__ == "__main__":
    main()
