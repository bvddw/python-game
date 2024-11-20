import pygame
from time import sleep
from random import uniform

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)

x, y = WIDTH // 2, HEIGHT // 2
radius = 10
velocity = 8
vx = velocity * uniform(-1, 1)
vy = velocity * uniform(-1, 1)

vp = 10

height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height

score = 0
num = 1.5

border_l = bound
border_r = WIDTH - bound
border_u = bound
border_d = HEIGHT - bound - height


def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = ''.join([chr(int(str(el), 8)) for el in [107, 141, 155, 145, 40, 157, 166, 145, 162]])
    a = Font.render(text, 1, (255, 255, 255))
    win.blit(a, (WIDTH // 2 - 70, HEIGHT // 3))
    pygame.display.update()


def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))
    pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))
    pygame.draw.rect(win, white, (xp, yp, width, height))
    pygame.draw.circle(win, (0, 255, 0), (x, y), radius)
    pygame.display.update()


run = True

while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x += vx
    y += vy

    if x - radius < border_l or x + radius > border_r:
        vx = -vx
    if y - radius < border_u:
        vy = -vy

    if y + vy >= yp:
        if xp <= x + vx <= xp + width:
            vy = -vy
            vx *= num
            vy *= num
            score += 1
        else:
            drawScore()
            sleep(10)
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
        xp += vp

    drawWindow()


pygame.quit()
