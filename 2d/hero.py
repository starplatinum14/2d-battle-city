import pygame
from settings import PLAYER_SPEED

class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, game_map):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.game_map = game_map
        self.old_rect = self.rect.copy()

    def update(self):
        self.check_collision()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.move(PLAYER_SPEED, 0)
        if keys[pygame.K_UP]:
            self.move(0, -PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            self.move(0, PLAYER_SPEED)

    def move(self, dx, dy):
        self.old_rect = self.rect.copy()
        self.rect.x += dx
        self.rect.y += dy

        obstacles_hit = pygame.sprite.spritecollide(self, self.game_map.obstacles, False)
        
        for obstacle in obstacles_hit:
            self.rect = self.old_rect
            return

    def check_collision(self):
        obstacles_hit = pygame.sprite.spritecollide(self, self.game_map.obstacles, False)
        
        for obstacle in obstacles_hit:
            self.rect = self.old_rect
            return
