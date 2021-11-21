import random
from sys import exit
import pygame

import enemy
from player import Player
from enemy import Enemy
from enemy_right import EnemyRight
from restart import Restart

pygame.init()
clock = pygame.time.Clock()
game_state = True
start_time = 0

######### font and text #########

###### screen #######
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
target_fps = 75

####### instantiating objects #######
restart = Restart()
player = Player()
player_group = pygame.sprite.GroupSingle()  # group
player_group.add(player)  # adds the player object to single Group
player.rect.x = screen_width / 2
player.rect.y = screen_height / 2

###### text group #######
text_group = pygame.sprite.Group()
text_group.add(restart)

###### enemy group ######
all_sprites = pygame.sprite.Group()
left_enemy = pygame.sprite.Group()
right_enemy = pygame.sprite.Group()

for i in range(10):
    enemies = Enemy(-100, random.randrange(720 - 30))
    all_sprites.add(left_enemy)
    left_enemy.add(enemies)

for i in range(10):
    enemy_r = EnemyRight(screen_width + 45, random.randrange(720 - 30))
    all_sprites.add(right_enemy)
    right_enemy.add(enemy_r)


######## Timer and display #########


def display_score():
    display_score_font = pygame.font.Font('fonts/rainyhearts.ttf', 100)
    display_score_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = display_score_font.render(f'Score: {display_score_time}', False, (221, 252, 255))
    score_rect = score_surface.get_rect(center=(screen_width / 2, 100))
    screen.blit(score_surface, score_rect)


def game_over():
    game_over_font = pygame.font.Font('fonts/rainyhearts.ttf', 100)
    game_over_surface = game_over_font.render('Game Over', False, (221, 252, 255))
    score_rect = game_over_surface.get_rect(center=(screen_width / 2, (screen_height / 2) - 100))
    screen.blit(game_over_surface, score_rect)
    gravity = 0
    gravity += 10
    for enemy_ri in right_enemy:  # iterates through the right enemy group and accesses its rect
        enemy_ri.rect.y += gravity
    for enemy_l in left_enemy:  # iterates through the left enemy group and accesses its rect
        enemy_l.rect.y += gravity
    player.rect.y += gravity


def restart_state():  # restarts everything's position to default for player
    if restart.rect.collidepoint(mouse_position) and mouse_press[0]:
        player.rect.x = screen_width / 2
        player.rect.y = screen_height / 2
        for enemy_ri in right_enemy:  # iterates through the right enemy group and accesses its rect
            enemy_ri.rect.x = screen_width + 45
            enemy_ri.rect.y = random.randrange(720 - 30)
        for enemy_l in left_enemy:  # iterates through the left enemy group and accesses its rect
            enemy_l.rect.x = -100
            enemy_l.rect.y = random.randrange(720 - 30)


def screen_move():
    gravity = 0
    gravity += 25
    for enemy_ri in right_enemy:  # iterates through the right enemy group and accesses its rect
        enemy_ri.rect.y += gravity
    for enemy_l in left_enemy:  # iterates through the left enemy group and accesses its rect
        enemy_l.rect.y += gravity


def user_inter():
    pass


###### game loop #######
running = True

while running:

    dt = clock.tick(75) * .001 * target_fps
    screen.fill((34, 54, 76))
    current_time = int(pygame.time.get_ticks() / 1000) - 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_key = True
            elif event.key == pygame.K_d:
                player.right_key = True
            elif event.key == pygame.K_SPACE and game_state:
                player.jump()
                # screen_move()
                if game_state and player.rect.y <= 250:
                    pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_key = False
            elif event.key == pygame.K_d:
                player.right_key = False

    collision = pygame.sprite.spritecollide(player, all_sprites, False)
    if game_state:
        display_score()
        ######PLAYER/UPDATE######
        player_group.draw(screen)
        player_group.update(dt)

        ######check enemy and player collision######
        player_hits = 0
        if collision:
            player.image.fill((235, 0, 0))
            player_hits += 1
            print(player_hits)

        else:
            player.image.fill((104, 153, 199))

        ######ENEMY######
        all_sprites.draw(screen)
        all_sprites.update()

    ##### when player dies #####
    if collision or player.rect.top > screen_height or player.rect.bottom < 0:
        game_state = False
        all_sprites.draw(screen)
        player_group.draw(screen)

    if not game_state:
        all_sprites.draw(screen)
        game_over()
        text_group.draw(screen)
        if restart.rect.collidepoint(restart.mouse_pos):
            print('aw')
        ###### mouse position #######
        mouse_position = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        ###### restarting enemy and player position #######
        if restart.rect.collidepoint(mouse_position) and mouse_press[0]:
            game_state = True
            start_time = int(pygame.time.get_ticks() / 1000) - 0
            user_inter()
            restart_state()

    pygame.display.update()
