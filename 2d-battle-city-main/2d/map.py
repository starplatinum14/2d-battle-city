import pygame
from enemy import Enemy

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((128, 128, 128))  # Сірий колір для перешкод
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Map:
    def __init__(self):
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.load_map("C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\map.txt")

    def load_map(self, filename):
        with open(filename, 'r') as f:
            for y, line in enumerate(f):
                for x, char in enumerate(line.strip()):
                    if (char == '#'):
                        obstacle = Obstacle(x * 50, y * 50)
                        self.obstacles.add(obstacle)
                    elif (char == 'E'):
                        enemy = Enemy(x * 50, y * 50, 'down', self.obstacles, self.bullets)  # Додано bullets_group
                        self.enemies.add(enemy)

    def draw(self, surface):
        self.obstacles.draw(surface)
        self.enemies.draw(surface)
        self.bullets.draw(surface)
