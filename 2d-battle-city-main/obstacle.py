import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((128, 128, 128))  # Сірий колір для перешкод
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
