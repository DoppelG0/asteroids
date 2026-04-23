import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    astfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        #player.draw(screen)
        dt = clock.tick(60) /1000
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
