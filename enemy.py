import random
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((45, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.image.fill((211, 59, 126))
        self.speedy = random.randrange(3, 8)
        self.speedx = random.randrange(8, 15)

    def enemy_movement(self):
        self.rect.x += self.speedx
        # self.rect.y += self.speedy
        if self.rect.left > 1280:
            self.rect.x = -100
            self.rect.y = random.randrange(720 - 30)

    def enemy_spawn(self):
        self.rect.x = -100
        self.rect.y = random.randrange(720 - 30)

    def update(self):
        self.enemy_movement()


