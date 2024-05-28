import pygame
from rectangle import Bar
import random
import argparse
from constants import *
from sys import exit


def pause_screen():
    display = True
    while display:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                display = False


def generateBars(n: int):
    width = int(S_WIDTH / n)

    out = []
    for i in range(0, S_WIDTH, width):
        value = random.randint(1, S_HEIGHT)
        temp = Bar(i, S_HEIGHT - value, width, value)
        out.append(temp)

    assert len(out) == n, f'{len(out)} != {n}'

    return out


def drawBars(bars, s, c):
    width = int(S_WIDTH / len(bars))
    for i, b in enumerate(bars):
        s.fill((0, 0, 0), (b.x, 0, b.w, 600))
        b.x = i * width
        b.render(s)
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


# def bubbleSort(bars):
#     n = len(bars)
#     for i in range(n):
#         for j in range(n - 1 - i):
#             screen.fill("black")
#
#             if bars[j].h > bars[j + 1].h:
#                 bars[j], bars[j + 1] = bars[j + 1], bars[j]
#
#             drawBars(bars)
#
#
# def mergeSort(bars, l=0, r=NLOGN):
#     if len(bars[l:r]) == 1:
#         return
#
#     m = (l + r) // 2
#
#     mergeSort(bars, l, m)
#     mergeSort(bars, m, r)
#
#     merge(l, r, m, bars, l)
#     drawBars(bars)
#
#
# def merge(l, r, m, bars, bI):
#     lArr = [(bars[i], i) for i in range(l, m)]
#     rArr = [(bars[i], i) for i in range(m, r)]
#
#     lI, rI = 0, 0
#
#     # out = []
#
#     while lI < len(lArr) and rI < len(rArr):
#         if lArr[lI][0].h < rArr[rI][0].h:
#             value, index = lArr[lI]
#             bars[bI] = value
#             lI += 1
#         else:
#             value, index = rArr[rI]
#             bars[bI] = value
#             rI += 1
#
#         # out.append(bars[index])
#         bI += 1
#         drawBars(bars)
#
#     while lI < len(lArr):
#         value, index = lArr[lI]
#         lI += 1
#         bars[bI] = value
#         # out.append(bars[index])
#         bI += 1
#         drawBars(bars)
#
#     while rI < len(rArr):
#         value, index = rArr[rI]
#         rI += 1
#         bars[bI] = value
#         # out.append(bars[index])
#         bI += 1
#         drawBars(bars)
#
#     # return bars
#
#
# def pivot(bars, l, r):
#     p = bars[r].h
#
#     cPos = l - 1
#     for i in range(l, r):
#         if bars[i].h <= p:
#             cPos += 1
#             bars[i], bars[cPos] = bars[cPos], bars[i]
#             drawBars(bars)
#
#     bars[cPos + 1], bars[r] = bars[r], bars[cPos + 1]
#     drawBars(bars)
#
#     return cPos + 1
#
#
# def quickSort(bars, l=0, r=NLOGN - 1):
#     if l >= r:
#         return
#
#     p = pivot(bars, l, r)
#     quickSort(bars, l, p - 1)
#     quickSort(bars, p + 1, r)
#     drawBars(bars)
#
#
# def bogoSort(bars):
#     while 1:
#         seen = set()
#
#         while len(seen) < len(bars) - 1:
#             a = random.randint(0, len(bars) - 1)
#             b = random.randint(0, len(bars) - 1)
#             while a in seen: a = random.randint(0, len(bars) - 1)
#             while b in seen: b = random.randint(0, len(bars) - 1)
#
#             seen.add(a)
#             seen.add(b)
#
#             bars[a], bars[b] = bars[b], bars[a]
#
#         drawBars(bars)
#
#         done = True
#         for i in range(len(bars) - 1):
#             if bars[i].h > bars[i + 1].h: done = False
#
#         if done:
#             break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Sort Visualizer',
        description='Visualizes various sorting algorithms',
        epilog='Author: Di Nguyen '
    )

    parser.add_argument('-e', '--elements', type=int, required=False, default=S_WIDTH / 2,
                        help='The number of elements '
                             'to sort ('
                             'must be a divisor of screen width)')
    parser.add_argument('-s', '--sort_name', required=False, default='bogo', help='Sorting algorithm to visualize')

    parser.add_argument('--width', required=False, default=S_WIDTH)
    parser.add_argument('--height', required=False, default=S_HEIGHT)
    parser.add_argument('--ls', action='store_true', default=False)

    args = parser.parse_args()

    known_sorts = {
        'bogo': bogoSort,
        'quick': quickSort,
        'merge': mergeSort,
        'bubble': bubbleSort
    }

    if args.ls:
        for name in known_sorts:
            print(name)
        exit(0)

    s_width = args.width
    s_height = args.height
    sort_name = args.sort_name
    N = args.elements

    assert s_width % args.elements == 0, f'elements ({n}) must be a divisor of screen width ({s_width})'
    assert sort_name in know_sorts, f'{sort_name} is not known --ls to view known sorts'

    # clock = pygame.time.Clock()
    # pygame.init()
    # screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    #
    # # sort_name = gui.inpoo
    # #
    # # if sort_name == 'h':
    # #     help_pressed = True
    # #     selected = True
    # # elif sort_name in known_sorts:
    # #     selected = True
    # #
    # # if not run:
    # #     break
    # #
    # # if selected and not help_pressed:
    # #     if sort_name in known_sorts:
    # #         complexity, func = known_sorts[sort_name]
    # #
    # #         bars = getBar(complexity)
    # #         func(bars=bars)
    # #         assert_correct(bars)
    # #         pause_screen()
    # #
    # #         gui.inpoo = ''
    # #         selected = False
    # pygame.quit()
