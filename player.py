import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect(midbottom=(500, 500))
        self.image.fill((104, 153, 199))
        self.screen_width = 1280
        self.screen_height = 720
        self.left_key, self.right_key = False, False
        self.is_jumping, self.on_ground = False, False
        self.velocity = 6
        self.gravity = 0

    def player_movement(self):
        if self.left_key:
            self.rect.left -= self.velocity
        if self.right_key:
            self.rect.right += self.velocity

    def player_border(self):
        if self.rect.right >= self.screen_width: self.rect.right = self.screen_width
        if self.rect.left <= 0: self.rect.left = 0
        # if self.rect.bottom >= self.screen_height: self.rect.bottom = self.screen_height
        # if self.rect.top <= 0: self.rect.top = 0

    def jump(self):
        if self.rect.bottom < self.screen_height:  # can only jump if player's y is < screen height
            self.is_jumping = True
            self.gravity -= 13  # makes player jump
            self.gravity = -7  # when player jumps the gravity is set to -7
            self.on_ground = False

    def apply_gravity(self):
        self.gravity += .4  # pulls player down
        self.rect.y += self.gravity  # increments the gravity by .4 every frame
        if self.gravity >= 12: self.gravity = 12  # set gravity to constant

    def update(self, dt):
        self.player_movement()
        self.player_border()
        self.apply_gravity()
