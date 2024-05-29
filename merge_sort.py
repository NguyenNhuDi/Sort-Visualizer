import constants
from utils import drawBars


def mergeSort(bars, s, c, l=0, r=constants.global_n):
    print(l, r)
    if len(bars[l:r]) == 1:
        return

    m = (l + r) // 2

    mergeSort(bars, s=s, c=c, l=m, r=m)
    mergeSort(bars, s=s, c=c, l=m, r=r)

    merge(l, r, m, bars, l, s, c)
    drawBars(bars, s, c)


def merge(l, r, m, bars, bI, s, c):
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

        # out.append(bars[index])
        bI += 1
        drawBars(bars, s, c)

    while lI < len(lArr):
        value, index = lArr[lI]
        lI += 1
        bars[bI] = value
        # out.append(bars[index])
        bI += 1
        drawBars(bars, s, c)

    while rI < len(rArr):
        value, index = rArr[rI]
        rI += 1
        bars[bI] = value
        # out.append(bars[index])
        bI += 1
        drawBars(bars, s, c)
