from utils import drawBars
from utils import drawCurrentBar

def radixSort(bars, s, c):
    num_to_pos = {}
    pos_to_num = {}

    # O(N)
    maxi_length = -1
    for bar in bars:
        maxi_length = max(maxi_length, len(str(bar.h)))

    # O(N)
    for i, bar in enumerate(bars):
        c_num = str(bar.h)

        while len(c_num) < maxi_length:
            c_num = '0' + c_num

        while c_num in num_to_pos:
            c_num = '0' + c_num

        num_to_pos[c_num] = i
        pos_to_num[i] = c_num

    for i in range(1, maxi_length + 1):
        stacks = [[] for _ in range(10)]

        # insert into stacks
        for index in pos_to_num:
            c_digit = int(pos_to_num[index][-i])

            stacks[c_digit].append(pos_to_num[index])

        ptr = 0
        for numbers in stacks:
            for curr_num in numbers:
                curr_index = num_to_pos[curr_num]

                swap_num = pos_to_num[ptr]

                bars[curr_index], bars[ptr] = bars[ptr], bars[curr_index]
                drawBars(bars, s, c)
                drawCurrentBar(bars[ptr], s, c)

                num_to_pos[curr_num] = ptr
                num_to_pos[swap_num] = curr_index

                pos_to_num[curr_index] = swap_num
                pos_to_num[ptr] = curr_num

                ptr += 1