import pygame

pygame.init()

w, l = 600, 600
screen = pygame.display.set_mode((w, l))
running = True

white = (255, 255, 255)
red = (255, 0, 0)
r = 25
x, y = 300, 300
FPS = 60
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20
    if x > 579: x -= 20
    if y > 579: y -= 20
    if x < 21: x += 20
    if y < 21: y += 20

    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), r)

    pygame.display.flip()
    clock.tick(FPS)