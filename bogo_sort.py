from utils import drawBars
import random


def bogoSort(bars, s, c):
    while 1:
        seen = set()

        while len(seen) < len(bars) - 1:
            a = random.randint(0, len(bars) - 1)
            b = random.randint(0, len(bars) - 1)

            while a in seen:
                a = random.randint(0, len(bars) - 1)

            while b in seen:
                b = random.randint(0, len(bars) - 1)

            seen.add(a)
            seen.add(b)

            bars[a], bars[b] = bars[b], bars[a]

        drawBars(bars, s, c)

        done = True
        for i in range(len(bars) - 1):
            if bars[i].h > bars[i + 1].h: done = False

        if done:
            break
