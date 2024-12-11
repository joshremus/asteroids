# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init
    print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Add sprite groups and add Player class to groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # Iniyialize Asteroid Field
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ticker = pygame.time.Clock()
    dt = 0.0

    # Initialise player object
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # iterate through the updateable group and update each object
        for each in updatable:
            each.update(dt)

        # Set background to black    
        screen.fill("black")    
        
        # iterate through the drawable group and update each object
        for item in drawable:
            item.draw(screen)
        #drawable.draw(screen)

        # reset the display
        pygame.display.flip()


        ttime = ticker.tick(60)
        dt = ttime / 1000

if __name__ == "__main__":
    main()