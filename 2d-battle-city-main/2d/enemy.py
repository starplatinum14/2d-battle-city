import pygame
import random
from settings import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, obstacles_group):
        super().__init__()
        self.image_up = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\enemy_up.png').convert_alpha()
        self.image_down = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\enemy_down.png').convert_alpha()
        self.image_left = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\enemy_left.png').convert_alpha()
        self.image_right = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\enemy_right.png').convert_alpha()


        self.image = self.image_down  # Початкове зображення - вниз
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = direction
        self.obstacles_group = obstacles_group  # Група перешкод
        pygame.transform.scale
    def update(self):
        if self.direction == 'left':
            self.image = self.image_left
            self.rect.x -= ENEMY_SPEED
        elif self.direction == 'right':
            self.image = self.image_right
            self.rect.x += ENEMY_SPEED
        elif self.direction == 'up':
            self.image = self.image_up
            self.rect.y -= ENEMY_SPEED
        elif self.direction == 'down':
            self.image = self.image_down
            self.rect.y += ENEMY_SPEED

        # Перевірка колізій з перешкодами
        self.check_collision()

    def check_collision(self):
        obstacles_hit = pygame.sprite.spritecollide(self, self.obstacles_group, False)
        
        for obstacle in obstacles_hit:
            # Виконати дії в разі зіткнення
            # Наприклад, змінити напрямок руху ворога
            self.change_direction()

    def change_direction(self):
        # Реалізуйте зміну напрямку руху ворога
        self.direction = random.choice(['left', 'right', 'up', 'down'])
