import random
import pygame
from db import get_personal_best
from ui import draw_text, WHITE, BLACK

# Настройки экрана
CELL_SIZE = 40
WIDTH = 800
HEIGHT = 700  # 640 для игры + 60 для панели
TOP_PANEL = 60
COLS = WIDTH // CELL_SIZE
ROWS = (HEIGHT - TOP_PANEL) // CELL_SIZE

# Цвета в стиле Snake Tax
BG_COLOR = (15, 20, 30)
GRID_COLOR = (22, 30, 42)
TEXT_GREEN = (90, 230, 140)

class SnakeGame:
    def __init__(self, screen, clock, username, settings):
        self.screen = screen
        self.clock = clock
        self.username = username
        self.settings = settings
        
        self.snake_color = tuple(settings.get("snake_color", (50, 170, 90)))
        self.grid_enabled = settings.get("grid", True)
        
        self.font = pygame.font.SysFont("consolas", 24, bold=True)
        self.font_small = pygame.font.SysFont("consolas", 18, bold=True)

        try:
            self.personal_best = get_personal_best(username)
        except: self.personal_best = 0

        self.snake = [(COLS//2, ROWS//2), (COLS//2-1, ROWS//2), (COLS//2-2, ROWS//2)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        
        self.score = 0
        self.level = 1
        self.game_over = False
        
        self.obstacles = []
        self.food = None
        self.spawn_food()

    def grid_to_pixel(self, pos):
        return pos[0] * CELL_SIZE, pos[1] * CELL_SIZE + TOP_PANEL

    def spawn_food(self):
        occupied = set(self.snake) | set(self.obstacles)
        free = [(c, r) for c in range(COLS) for r in range(ROWS) if (c, r) not in occupied]
        if not free: return
        pos = random.choice(free)
        self.food = {
            "pos": pos, 
            "weight": random.randint(1, 3), 
            "spawn_time": pygame.time.get_ticks(),
            "timer": 5000
        }

    def draw(self):
        self.screen.fill(BG_COLOR)
        now = pygame.time.get_ticks()

        # Отрисовка сетки (Grid)
        for c in range(COLS):
            for r in range(ROWS):
                rx, ry = c * CELL_SIZE, r * CELL_SIZE + TOP_PANEL
                pygame.draw.rect(self.screen, GRID_COLOR, (rx+1, ry+1, CELL_SIZE-2, CELL_SIZE-2), border_radius=4)

        # Верхняя панель (HUD)
        pygame.draw.rect(self.screen, (10, 15, 25), (0, 0, WIDTH, TOP_PANEL))
        pygame.draw.line(self.screen, (50, 60, 80), (0, TOP_PANEL), (WIDTH, TOP_PANEL), 2)

        # Текст (Score, Best, Timer)
        score_surf = self.font.render(f"SCORE: {self.score}", True, TEXT_GREEN)
        best_surf = self.font.render(f"BEST: {self.personal_best}", True, (150, 170, 150))
        self.screen.blit(score_surf, (20, 15))
        self.screen.blit(best_surf, (220, 15))

        time_left = max(0, (self.food["timer"] - (now - self.food["spawn_time"])) // 1000)
        timer_surf = self.font.render(f"ENDS IN: {time_left}S", True, (255, 100, 100))
        self.screen.blit(timer_surf, (WIDTH - 180, 15))

        # Еда
        fx, fy = self.grid_to_pixel(self.food["pos"])
        f_color = (220, 60, 60) if self.food["weight"] == 1 else (255, 215, 0)
        pygame.draw.rect(self.screen, f_color, (fx+4, fy+4, CELL_SIZE-8, CELL_SIZE-8), border_radius=10)
        w_txt = self.font_small.render(str(self.food["weight"]), True, WHITE)
        self.screen.blit(w_txt, (fx + 15, fy + 12))

        # Препятствия
        for obs in self.obstacles:
            ox, oy = self.grid_to_pixel(obs)
            pygame.draw.rect(self.screen, (70, 80, 100), (ox+2, oy+2, CELL_SIZE-4, CELL_SIZE-4), border_radius=2)

        # Змейка
        for i, seg in enumerate(self.snake):
            sx, sy = self.grid_to_pixel(seg)
            color = (100, 255, 150) if i == 0 else self.snake_color
            pygame.draw.rect(self.screen, color, (sx+2, sy+2, CELL_SIZE-4, CELL_SIZE-4), border_radius=6)

    def move(self):
        now = pygame.time.get_ticks()
        if now - self.food["spawn_time"] > self.food["timer"]:
            self.spawn_food()

        self.direction = self.next_direction
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in self.snake or head in self.obstacles:
            self.game_over = True
            return

        self.snake.insert(0, head)
        if head == self.food["pos"]:
            self.score += 10 * self.food["weight"]
            if self.score // 100 >= self.level:
                self.level += 1
                # Добавляем препятствие при повышении уровня
                self.obstacles.append((random.randint(0, COLS-1), random.randint(0, ROWS-1)))
            self.spawn_food()
        else:
            self.snake.pop()

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: return "quit", self.score, self.level
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_w] and self.direction != (0, 1): self.next_direction = (0, -1)
                    if event.key in [pygame.K_DOWN, pygame.K_s] and self.direction != (0, -1): self.next_direction = (0, 1)
                    if event.key in [pygame.K_LEFT, pygame.K_a] and self.direction != (1, 0): self.next_direction = (-1, 0)
                    if event.key in [pygame.K_RIGHT, pygame.K_d] and self.direction != (-1, 0): self.next_direction = (1, 0)

            self.move()
            self.draw()
            pygame.display.flip()
            self.clock.tick(5 + self.level)

        return "game_over", self.score, self.level