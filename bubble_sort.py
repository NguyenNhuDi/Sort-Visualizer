from utils import drawBars
from utils import drawCurrentBar


def bubbleSort(bars, s, c):
    n = len(bars)
    for i in range(n):
        for j in range(n - 1 - i):
            s.fill("black")

            if bars[j].h > bars[j + 1].h:
                bars[j], bars[j + 1] = bars[j + 1], bars[j]

            drawBars(bars, s, c)
            drawCurrentBar(bars[j], s, c)
