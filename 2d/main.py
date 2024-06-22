import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from hero import Hero
from enemy import Enemy
from map import Map

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Battle City Remake')

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    game_map = Map()
    hero = Hero(100, 100, game_map)  # Тепер використовуємо клас Hero
    all_sprites.add(hero)

    all_sprites.add(game_map.enemies)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill(BLACK)
        game_map.draw(screen)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
