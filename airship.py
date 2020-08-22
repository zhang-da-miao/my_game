import pygame


class Ship():
    def __init__(self, screen):
        """初始化飞船并设置位置"""
        self.screen = screen

        self.image = pygame.image.load('images/antmaker.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitime(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
