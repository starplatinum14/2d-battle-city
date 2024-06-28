import pygame
import random
from settings import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_COOLDOWN
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, game_map):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # червоний квадрат
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.change_direction_time = pygame.time.get_ticks()
        self.last_shot_time = pygame.time.get_ticks()
        self.game_map = game_map

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.change_direction_time > 1000:
            self.direction = random.choice(['left', 'right', 'up', 'down'])
            self.change_direction_time = now

        if now - self.last_shot_time > BULLET_COOLDOWN:
            self.shoot()
            self.last_shot_time = now

        self.move()

    def move(self):
        old_rect = self.rect.copy()

        if self.direction == 'left':
            self.rect.x -= ENEMY_SPEED
        elif self.direction == 'right':
            self.rect.x += ENEMY_SPEED
        elif self.direction == 'up':
            self.rect.y -= ENEMY_SPEED
        elif self.direction == 'down':
            self.rect.y += ENEMY_SPEED

        if pygame.sprite.spritecollideany(self, self.game_map.obstacles):
            self.rect = old_rect
            self.direction = random.choice(['left', 'right', 'up', 'down'])

        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = random.choice(['right', 'up', 'down'])
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.direction = random.choice(['left', 'up', 'down'])
        if self.rect.top < 0:
            self.rect.top = 0
            self.direction = random.choice(['left', 'right', 'down'])
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.direction = random.choice(['left', 'right', 'up'])

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction, self)
        self.game_map.bullets.add(bullet)
