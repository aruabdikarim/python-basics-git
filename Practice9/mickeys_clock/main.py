import pygame
from clock import get_time_angles

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# центр часов
center = (WIDTH // 2, HEIGHT // 2)

# загрузка изображения
hand_img = pygame.image.load("images/hand.png").convert_alpha()
hand_img = pygame.transform.scale(hand_img, (50, 200))


def rotate(image, angle, center):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect


running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sec_angle, min_angle = get_time_angles()

    # секунды (левая рука)
    sec_hand, sec_rect = rotate(hand_img, sec_angle, center)

    # минуты (правая рука)
    min_hand, min_rect = rotate(hand_img, min_angle, center)

    screen.blit(sec_hand, sec_rect)
    screen.blit(min_hand, min_rect)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()