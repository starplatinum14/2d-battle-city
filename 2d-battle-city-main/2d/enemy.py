import pygame
import random
from settings import ENEMY_SPEED, BULLET_SPEED
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, obstacles_group, bullets_group):
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
        self.bullets_group = bullets_group  # Група куль
        self.shoot_timer = 0  # Ініціалізація таймера для стрільби

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

        self.check_collision()
        self.shoot()  # Виклик методу стрільби

    def check_collision(self):
        obstacles_hit = pygame.sprite.spritecollide(self, self.obstacles_group, False)
        
        for obstacle in obstacles_hit:
            self.change_direction()

    def change_direction(self):
        self.direction = random.choice(['left', 'right', 'up', 'down'])

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shoot_timer > 2000:  # Стріляти кожні 2 секунди
            self.shoot_timer = now
            if self.direction == 'left':
                bullet = Bullet(self.rect.left, self.rect.centery, 'left', self)
            elif self.direction == 'right':
                bullet = Bullet(self.rect.right, self.rect.centery, 'right', self)
            elif self.direction == 'up':
                bullet = Bullet(self.rect.centerx, self.rect.top, 'up', self)
            elif self.direction == 'down':
                bullet = Bullet(self.rect.centerx, self.rect.bottom, 'down', self)
            self.bullets_group.add(bullet)
