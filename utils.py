import pygame
from rectangle import Bar
import random
import constants


def pause_screen():
    display = True
    while display:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                display = False


def generateBars(n: int):
    print(n)
    width = int(constants.global_s_width / n)
    out = []
    for i in range(0, constants.global_s_width, width):
        value = random.randint(1, constants.global_s_height)
        temp = Bar(i, constants.global_s_height - value, width, value)
        out.append(temp)

    return out


def drawBars(bars, s, c):
    width = int(constants.global_s_width / len(bars))
    for i, b in enumerate(bars):
        b.x = i * width
        s.fill((0, 0, 0), (b.x, 0, b.w, constants.global_s_height))
        b.render(s)
    pygame.display.flip()
    c.tick(960)


def drawCurrentBar(bar, s, c):
    bar.render_red(s)
    pygame.display.flip()
    c.tick(960)


def getBar(n, s, c):
    b = generateBars(n)
    drawBars(b, s, c)
    pause_screen()
    return b


def assert_correct(bars, s, c):
    for i in range(len(bars) - 1):
        assert bars[i].h <= bars[i + 1].h
        bars[i].render_correct(s)
        pygame.display.flip()
        c.tick(120)

    bars[-1].render_correct(s)
    pygame.display.flip()
    c.tick(120)
