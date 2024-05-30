import constants
from utils import drawBars
from utils import drawCurrentBar


def mergeSort(bars, s, c, l=None, r=None):
    if r is None:
        r = constants.global_n

    if l is None:
        l = 0

    if len(bars[l:r]) <= 1:
        return

    m = (l + r) // 2

    mergeSort(bars, s=s, c=c, l=l, r=m)
    mergeSort(bars, s=s, c=c, l=m, r=r)

    merge(l, r, m, bars, l, s, c)
    drawBars(bars, s, c)


def merge(l, r, m, bars, bI, s, c):
    # print(l,m,r, len(bars))

    lArr = [(bars[i], i) for i in range(l, m)]
    rArr = [(bars[i], i) for i in range(m, r)]

    lI, rI = 0, 0

    # out = []

    while lI < len(lArr) and rI < len(rArr):
        if lArr[lI][0].h < rArr[rI][0].h:
            value, index = lArr[lI]
            bars[bI] = value
            lI += 1
        else:
            value, index = rArr[rI]
            bars[bI] = value
            rI += 1

        drawBars(bars, s, c)
        drawCurrentBar(bars[bI], s, c)
        bI += 1

    while lI < len(lArr):
        value, index = lArr[lI]
        lI += 1
        bars[bI] = value

        drawBars(bars, s, c)
        drawCurrentBar(bars[bI], s, c)

        bI += 1

    while rI < len(rArr):
        value, index = rArr[rI]
        rI += 1
        bars[bI] = value

        drawBars(bars, s, c)
        drawCurrentBar(bars[bI], s, c)

        bI += 1
