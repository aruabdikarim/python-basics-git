import pygame
import sys
from db import create_tables, save_result, get_personal_best, get_top_scores
from settings_manager import load_settings, save_settings
from game import SnakeGame, WIDTH, HEIGHT
from ui import Button, draw_text, get_username, BIG_FONT, FONT
from ui import BLACK, BLUE, GREEN, RED, YELLOW, WHITE

# Инициализация
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Попытка загрузить музыку (если файла нет, игра не вылетит)
try:
    snake_music = pygame.mixer.Sound("snake_sound.mp3")
    snake_music.play(-1)
except:
    print("Music file not found, playing without sound.")
    snake_music = None

def main_menu():
    btn_w = 220
    cx = (WIDTH // 2) - (btn_w // 2)
    
    buttons = {
        "play": Button("Play", (cx, 220, btn_w, 55), GREEN),
        "leaderboard": Button("Leaderboard", (cx, 295, btn_w, 55), BLUE),
        "settings": Button("Settings", (cx, 370, btn_w, 55), BLUE),
        "quit": Button("Quit", (cx, 445, btn_w, 55), RED),
    }

    while True:
        screen.fill((15, 20, 30)) # Темный фон в стиле игры

        draw_text(screen, "SNAKE PRO", WIDTH // 2, 100, WHITE, BIG_FONT, center=True)
        draw_text(screen, "Database & Levels Edition", WIDTH // 2, 160, (90, 230, 140), FONT, center=True)

        for button in buttons.values():
            button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            for action, button in buttons.items():
                if button.is_clicked(event):
                    return action

        pygame.display.flip()
        clock.tick(60)

def leaderboard_screen():
    btn_w = 200
    back_button = Button("Back", ((WIDTH // 2) - (btn_w // 2), 620, btn_w, 50), RED)

    while True:
        screen.fill((20, 25, 35))
        draw_text(screen, "TOP 10 PLAYERS", WIDTH // 2, 60, WHITE, BIG_FONT, center=True)

        # Заголовки таблицы
        y = 150
        draw_text(screen, "Rank  User       Score   Lvl", 50, y, (150, 170, 150), FONT)
        
        try:
            rows = get_top_scores()
        except:
            rows = []

        y += 50
        for i, row in enumerate(rows[:10], start=1):
            username, score, level, _ = row
            draw_text(screen, f"{i}.    {username[:8]:<10} {score:<7} {level}", 50, y, WHITE, FONT)
            y += 40

        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "quit"
            if back_button.is_clicked(event): return "menu"

        pygame.display.flip()
        clock.tick(60)

def game_over_screen(username, score, level):
    btn_w = 220
    cx = (WIDTH // 2) - (btn_w // 2)
    
    retry_button = Button("Retry", (cx, 400, btn_w, 55), GREEN)
    menu_button = Button("Main Menu", (cx, 475, btn_w, 55), BLUE)

    try:
        best = get_personal_best(username)
    except:
        best = score

    while True:
        screen.fill((15, 20, 30))

        draw_text(screen, "GAME OVER", WIDTH // 2, 130, RED, BIG_FONT, center=True)
        draw_text(screen, f"Player: {username}", WIDTH // 2, 210, WHITE, FONT, center=True)
        draw_text(screen, f"Score: {score}  |  Level: {level}", WIDTH // 2, 260, (90, 230, 140), FONT, center=True)
        draw_text(screen, f"Personal Best: {best}", WIDTH // 2, 310, (150, 170, 150), FONT, center=True)

        retry_button.draw(screen)
        menu_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "quit"
            if retry_button.is_clicked(event): return "retry"
            if menu_button.is_clicked(event): return "menu"

        pygame.display.flip()
        clock.tick(60)

def settings_screen(settings):
    btn_w = 300
    cx = (WIDTH // 2) - (btn_w // 2)
    
    grid_btn = Button("", (cx, 200, btn_w, 50), BLUE)
    sound_btn = Button("", (cx, 280, btn_w, 50), BLUE)
    save_btn = Button("Save & Back", (cx, 450, btn_w, 55), GREEN)

    while True:
        screen.fill((20, 25, 35))
        draw_text(screen, "SETTINGS", WIDTH // 2, 90, WHITE, BIG_FONT, center=True)

        grid_btn.text = f"Grid: {'ON' if settings['grid'] else 'OFF'}"
        sound_btn.text = f"Sound: {'ON' if settings['sound'] else 'OFF'}"

        grid_btn.draw(screen)
        sound_btn.draw(screen)
        save_btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "quit"
            if grid_btn.is_clicked(event):
                settings["grid"] = not settings["grid"]
            if sound_btn.is_clicked(event):
                settings["sound"] = not settings["sound"]
                if snake_music:
                    snake_music.set_volume(1 if settings["sound"] else 0)
            if save_btn.is_clicked(event):
                save_settings(settings)
                return "menu"

        pygame.display.flip()
        clock.tick(60)

def play_game(settings):
    username = get_username(screen, clock, WIDTH, HEIGHT)
    if not username: return "menu"

    while True:
        game = SnakeGame(screen, clock, username, settings)
        status, score, level = game.run()

        if status == "quit": return "quit"

        try:
            save_result(username, score, level)
        except:
            pass

        action = game_over_screen(username, score, level)
        if action == "retry": continue
        return action

def main():
    try:
        create_tables()
    except:
        pass

    settings = load_settings()
    if snake_music:
        snake_music.set_volume(1 if settings.get("sound", True) else 0)

    while True:
        action = main_menu()
        if action == "quit": break
        elif action == "play":
            if play_game(settings) == "quit": break
        elif action == "leaderboard":
            if leaderboard_screen() == "quit": break
        elif action == "settings":
            if settings_screen(settings) == "quit": break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()