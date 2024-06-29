import pygame
from settings import BULLET_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, shooter):
        super().__init__()
        self.direction = direction
        self.shooter = shooter
        self.load_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def load_image(self):
        if self.direction == 'up':
            self.image = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\bullet_up.png')
        elif self.direction == 'down':
            self.image = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\bullet_down.png')
        elif self.direction == 'left':
            self.image = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\bullet_left.png')
        elif self.direction == 'right':
            self.image = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\bullet_right.png')
        self.image = pygame.transform.scale(self.image, (10, 10))  # Змінюємо розмір зображення до потрібного

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
