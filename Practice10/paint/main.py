import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

canvas = pygame.Surface(screen.get_size())
canvas.fill((0, 0, 0))

mode = "brush"
color = (0, 0, 255)
radius = 5

drawing = False
start = (0, 0)
last = (0, 0)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if e.key == pygame.K_1:
                mode = "brush"
            if e.key == pygame.K_2:
                mode = "rect"
            if e.key == pygame.K_3:
                mode = "circle"
            if e.key == pygame.K_4:
                mode = "eraser"
            if e.key == pygame.K_r:
                color = (255, 0, 0)
            if e.key == pygame.K_g:
                color = (0, 255, 0)
            if e.key == pygame.K_b:
                color = (0, 0, 255)
            if e.key == pygame.K_w:
                color = (255, 255, 255)

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            drawing = True
            start = last = e.pos

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            drawing = False
            end = e.pos

            if mode == "rect":
                pygame.draw.rect(canvas, color, (*start, end[0]-start[0], end[1]-start[1]), 2)

            if mode == "circle":
                r = int(((end[0]-start[0])**2 + (end[1]-start[1])**2) ** 0.5)
                pygame.draw.circle(canvas, color, start, r, 2)

        if e.type == pygame.MOUSEMOTION and drawing:
            if mode in ("brush", "eraser"):
                draw_color = (0, 0, 0) if mode == "eraser" else color
                pygame.draw.line(canvas, draw_color, last, e.pos, radius)
                last = e.pos

    screen.blit(canvas, (0, 0))
    pygame.display.flip()
    clock.tick(60)