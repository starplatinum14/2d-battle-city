import pygame
from settings import BULLET_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, shooter):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))  # жовта куля
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.shooter = shooter

    def update(self):
        if self.direction == 'left':
            self.rect.x -= BULLET_SPEED
        elif self.direction == 'right':
            self.rect.x += BULLET_SPEED
        elif self.direction == 'up':
            self.rect.y -= BULLET_SPEED
        elif self.direction == 'down':
            self.rect.y += BULLET_SPEED

        # Видалити кулю, якщо вона виходить за межі екрану
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
