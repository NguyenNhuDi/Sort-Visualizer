from utils import drawBars
from utils import drawCurrentBar
from utils import drawBar


def selectionSort(bars, s, c):
    for i in range(len(bars)):
        mini = 0xffffffff
        mIndex = -1
        for j in range(i, len(bars)):
            if bars[j].h < mini:
                mini = bars[j].h
                mIndex = j

            drawBar(bars[j - 1], s, c)
            drawCurrentBar(bars[j], s, c)

        bars[i], bars[mIndex] = bars[mIndex], bars[i]

        drawBars(bars, s, c)
