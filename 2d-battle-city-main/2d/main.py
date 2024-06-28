import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from hero import Hero
from enemy import Enemy
from map import Map
from bullet import Bullet

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Battle City Remake')

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()  # Додаємо групу для куль

    game_map = Map()
    hero = Hero(100, 100, game_map)
    all_sprites.add(hero)
    enemies.add(game_map.enemies)
    all_sprites.add(game_map.enemies)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        bullets.update()

        screen.fill(BLACK)
        game_map.draw(screen)
        all_sprites.draw(screen)
        bullets.draw(screen)  # Додаємо відображення куль

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
