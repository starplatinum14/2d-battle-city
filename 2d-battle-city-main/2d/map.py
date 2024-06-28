import pygame
from pygame.sprite import Sprite
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy

class Obstacle(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # синій квадрат
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Map:
    def __init__(self):
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.load_map("map.txt")

    def load_map(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                if char == '#':
                    obstacle = Obstacle(x * 50, y * 50)
                    self.obstacles.add(obstacle)
                elif char == 'E':
                    enemy = Enemy(x * 50, y * 50, self)
                    self.enemies.add(enemy)

    def draw(self, screen):
        self.obstacles.draw(screen)
        self.enemies.draw(screen)
        self.bullets.draw(screen)
