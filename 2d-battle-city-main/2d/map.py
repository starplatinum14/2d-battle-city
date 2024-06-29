import pygame
from pygame.sprite import Sprite
from enemy import Enemy

class Map:
    def __init__(self):
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.load_map("C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\map.txt")

    def load_map(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                if char == '#':
                    obstacle = pygame.sprite.Sprite()
                    obstacle.image = pygame.Surface((50, 50))
                    obstacle.image.fill((0, 0, 255))  # синій квадрат
                    obstacle.rect = obstacle.image.get_rect()
                    obstacle.rect.topleft = (x * 50, y * 50)
                    self.obstacles.add(obstacle)
                elif char == 'E':
                    enemy = Enemy(x * 50, y * 50, 'left' , self.obstacles)
                    self.enemies.add(enemy)

    def draw(self, screen):
        self.obstacles.draw(screen)
        self.enemies.draw(screen)
