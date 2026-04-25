import pygame
import random
import sys
import os

pygame.init()

# Размеры
CELL = 40
COLS = 20
ROWS = 16
W = COLS * CELL
H = ROWS * CELL + 60

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Levels")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 24)
font_big = pygame.font.Font(None, 44)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load(name):
    for ext in [".png", ".jpg", ".jpeg", ".bmp"]:
        path = os.path.join(BASE_DIR, "images", name + ext)
        if os.path.isfile(path):
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.smoothscale(img, (CELL, CELL))
    return None

img_head = load("head")
img_body = load("body")
img_food = load("food")

def draw_cell(x, y, img, color):
    rx = x * CELL
    ry = y * CELL + 60
    if img:
        screen.blit(img, (rx, ry))
    else:
        pygame.draw.rect(screen, color, (rx + 2, ry + 2, CELL - 4, CELL - 4), border_radius=6)

def angle(d):
    return {(1,0): 270, (-1,0): 90, (0,-1): 0, (0,1): 180}[d]

def get_level(score):
    return score // 50 + 1

def get_speed(level):
    return max(60, 150 - (level - 1) * 15)

def get_walls(level):
    walls = []
    if level >= 2:
        for y in range(4, 12):
            walls.append((10, y))
    if level >= 3:
        for x in range(5, 15):
            walls.append((x, 8))
    if level >= 4:
        for x in range(COLS):
            walls.append((x, 0))
            walls.append((x, ROWS-1))
        for y in range(ROWS):
            walls.append((0, y))
            walls.append((COLS-1, y))
    return walls

def spawn_food(snake, walls):
    free = [(c, r) for c in range(COLS) for r in range(ROWS)
            if (c, r) not in snake and (c, r) not in walls]
    return random.choice(free)

def new_game():
    cx, cy = COLS // 2, ROWS // 2
    snake = [(cx, cy), (cx-1, cy), (cx-2, cy)]
    direction = (1, 0)
    level = 1
    walls = get_walls(level)
    food = spawn_food(snake, walls)
    return snake, direction, food, 0, level

snake, direction, food, score, level = new_game()
next_dir = direction
hi = 0
alive = True
speed = 150
last_move = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            keys = {
                pygame.K_UP: (0,-1), pygame.K_w: (0,-1),
                pygame.K_DOWN: (0,1), pygame.K_s: (0,1),
                pygame.K_LEFT: (-1,0), pygame.K_a: (-1,0),
                pygame.K_RIGHT: (1,0), pygame.K_d: (1,0),
            }
            if event.key in keys:
                nd = keys[event.key]
                if nd[0] + direction[0] != 0 or nd[1] + direction[1] != 0:
                    next_dir = nd

            if event.key == pygame.K_r and not alive:
                snake, direction, food, score, level = new_game()
                next_dir = direction
                alive = True

    level = get_level(score)
    speed = get_speed(level)
    walls = get_walls(level)

    now = pygame.time.get_ticks()
    if alive and now - last_move > speed:
        last_move = now
        direction = next_dir
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (not (0 <= head[0] < COLS and 0 <= head[1] < ROWS)
            or head in snake[:-1]
            or head in walls):
            alive = False
        else:
            snake.insert(0, head)

            if head == food:
                score += 10
                hi = max(hi, score)
                food = spawn_food(snake, walls)
            else:
                snake.pop()

    # ---- Отрисовка ----
    screen.fill((15, 20, 30))

    # Панель
    screen.blit(font.render(f"Счёт: {score}", True, (90, 230, 140)), (16, 18))
    screen.blit(font.render(f"Рекорд: {hi}", True, (150, 170, 150)), (200, 18))
    screen.blit(font.render(f"Уровень: {level}", True, (200, 200, 90)), (400, 18))
    screen.blit(font.render("R — рестарт", True, (70, 90, 80)), (W - 190, 18))

    # Сетка
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, (22, 30, 42),
                (c*CELL+1, r*CELL+61, CELL-2, CELL-2), border_radius=4)

    # Стены
    for w in walls:
        pygame.draw.rect(screen, (120, 120, 120),
            (w[0]*CELL+2, w[1]*CELL+62, CELL-4, CELL-4), border_radius=4)

    # Еда
    draw_cell(food[0], food[1], img_food, (220, 60, 60))

    # Тело
    for seg in snake[1:]:
        draw_cell(seg[0], seg[1], img_body, (50, 170, 90))

    # Голова
    hx, hy = snake[0]
    if img_head:
        rotated = pygame.transform.rotate(img_head, angle(direction))
        screen.blit(rotated, (hx * CELL, hy * CELL + 60))
    else:
        draw_cell(hx, hy, None, (80, 220, 120))

    # Game Over
    if not alive:
        overlay = pygame.Surface((W, H - 60), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 60))

        text1 = font_big.render("GAME OVER", True, (230, 70, 70))
        screen.blit(text1, text1.get_rect(center=(W//2, H//2 - 20)))

        text2 = font.render(f"Счёт: {score} | Нажми R", True, (200, 200, 200))
        screen.blit(text2, text2.get_rect(center=(W//2, H//2 + 30)))

    pygame.display.flip()
    clock.tick(60)