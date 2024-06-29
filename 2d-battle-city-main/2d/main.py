import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from hero import Hero
from enemy import Enemy
from map import Map
from button import Button

def start_game():
    game_map = Map()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(game_map.obstacles)
    all_sprites.add(game_map.enemies)
    all_sprites.add(game_map.bullets)

    hero = Hero(100, 100, game_map)
    all_sprites.add(hero)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill(BLACK)
        game_map.draw(screen)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def quit_game():
    pygame.quit()
    sys.exit()

def main_menu():
    try:
        background = pygame.image.load('C:\\Users\\nikit\\OneDrive\\Робочий стіл\\2d-battle-city-main\\2d\\background.jpg')
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except pygame.error as e:
        print(f"Не вдалося завантажити зображення: {e}")
        background = None

    start_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50, "Почати гру", start_game)
    quit_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 20, 200, 50, "Завершити гру", quit_game)

    buttons = [start_button, quit_button]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit_game()
            for button in buttons:
                button.handle_event(event)

        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill(BLACK)

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Battle City Remake')
    clock = pygame.time.Clock()

    main_menu()
