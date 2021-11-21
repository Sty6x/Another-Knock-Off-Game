import pygame.sprite
import random


class EnemyRight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((45, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.image.fill((0, 255, 0))
        self.speedy = random.randrange(3, 8)
        self.speedx = random.randrange(8, 15)

    def enemy_movement(self):
        self.rect.x -= self.speedx
        # self.rect.y += self.speedy
        if self.rect.right < 0:
            self.rect.x = 1280 + 30
            self.rect.y = random.randrange(720 - 30)


    def update(self):
        self.enemy_movement()
