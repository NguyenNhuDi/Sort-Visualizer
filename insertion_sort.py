from utils import drawBar
from utils import drawBars
from utils import drawCurrentBar


def insertionSort(bars, s, c):
    for i in range(len(bars)):
        if i == 0:
            continue

        ptr = i

        while ptr >= 1 and bars[ptr].h < bars[ptr - 1].h:
            bars[ptr], bars[ptr - 1] = bars[ptr - 1], bars[ptr]

            if ptr < len(bars) - 1:
                drawBar(bars[ptr + 1], s, c)

            drawCurrentBar(bars[ptr], s, c)

            ptr -= 1

        drawCurrentBar(bars[i], s, c)
        drawBars(bars, s, c)
