from utils import drawBars


def stalinSort(bars, s, c):
    ptr = 1
    while ptr < len(bars):

        while ptr < len(bars) and bars[ptr].h < bars[ptr - 1].h:
            bars.pop(ptr)
            drawBars(bars, s, c)

        drawBars(bars, s, c)
        ptr += 1
