import pygame
import sys
from settings import Settings


def run_game():
    pygame.init()
    ai_set = Settings()
    screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_set.bg_color)
        pygame.display.flip()


run_game()
