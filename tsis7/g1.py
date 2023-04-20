import pygame as pg
from datetime import datetime

pg.init()

FPS = 1

screen = pg.display.set_mode((700, 650))
clock = pg.time.Clock()

image = pg.image.load('lh.png')
image2 = pg.image.load('rh.png')

image1 = pg.image.load('clock.jpg')
image1 = pg.transform.scale(image1, (700, 650))


def blitRotate(surf, image, pos, angle):
    r_image = pg.transform.rotate(image, angle)
    rect = image.get_rect(center=pos)

    rot_rect = r_image.get_rect(center=rect.center)
    surf.blit(r_image, rot_rect)


sec2 = datetime.now().strftime('%S')
sec = datetime.now().strftime('%M')
angle = int(sec) * -6
angle2 = int(sec2) * -6
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(image1, (20, 20))

    sec2 = datetime.now().strftime('%M')
    sec = datetime.now().strftime('%S')
    angle = int(sec) * -6
    angle2 = int(sec2) * -6

    blitRotate(screen, image, (369, 337), angle)
    blitRotate(screen, image2, (369, 337), angle2)

    pg.display.update()
pg.quit()