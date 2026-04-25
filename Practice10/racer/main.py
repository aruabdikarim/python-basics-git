import pygame
import random
import sys
import os

pygame.init()

W, H = 600, 700
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Simple Racer")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

player_img = pygame.transform.scale(pygame.image.load("Practice10/racer/images/car.png"), (100, 120))
enemy_img = pygame.transform.scale(pygame.image.load("Practice10/racer/images/enemy.png"), (100, 120))
coin_img = pygame.transform.scale(pygame.image.load("Practice10/racer/images/coin.png"), (40, 40))
bg = pygame.transform.scale(pygame.image.load("Practice10/racer/images/AnimatedStreet.png").convert(), (W, H))

player = player_img.get_rect(center=(W//2, H - 100))
enemy = enemy_img.get_rect(center=(random.randint(50, W-50), -100))
coin = coin_img.get_rect(center=(random.randint(50, W-50), -300))

speed = 5
score = 0
coins = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 6
    if keys[pygame.K_RIGHT] and player.right < W:
        player.x += 6
    def hb(rect):
        return rect.inflate(-30, -30)
    enemy.y += speed
    if enemy.top > H:
        enemy.y = -100
        enemy.x = random.randint(50, W-50)
        score += 1
        speed += 0.2

    coin.y += speed
    if coin.top > H:
        coin.y = -300
        coin.x = random.randint(50, W-50)

    if hb(player).colliderect(hb(enemy)):
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    if player.colliderect(coin):
        coins += 1
        coin.y = -300
        coin.x = random.randint(50, W-50)

    screen.blit(bg, (0, 0))
    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)
    screen.blit(coin_img, coin)

    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10, 10))
    screen.blit(font.render(f"Coins: {coins}", True, (255,255,255)), (10, 50))

    pygame.display.update()
    clock.tick(60)