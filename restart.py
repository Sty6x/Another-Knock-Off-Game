import pygame.sprite
import random


class Restart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font_size = 70
        self.font = pygame.font.Font('fonts/rainyhearts.ttf', self.font_size)
        self.image = self.font.render('restart?', False, (221, 252, 255))
        self.rect = self.image.get_rect(center=(1280 / 2, (720 / 2)))
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_press = pygame.mouse.get_pressed()

    # def reset_position(self, screen):
    #     self.font.render('restart?', False, (221, 0, 0))
    #     screen.blit(self.image, self.rect)
    #
