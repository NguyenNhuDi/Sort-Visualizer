from constants import global_n
from utils import drawBars


def pivot(bars, l, r, s, c):
    p = bars[r].h

    cPos = l - 1
    for i in range(l, r):
        if bars[i].h <= p:
            cPos += 1
            bars[i], bars[cPos] = bars[cPos], bars[i]
            drawBars(bars, s, c)

    bars[cPos + 1], bars[r] = bars[r], bars[cPos + 1]
    drawBars(bars, s, c)

    return cPos + 1


def quickSort(bars, s, c, l=0, r=global_n - 1):
    if l >= r:
        return

    p = pivot(bars, l, r, s, c)
    quickSort(bars, s, c, l, p - 1)
    quickSort(bars, s, c, p + 1, r)
    drawBars(bars, s, c)
