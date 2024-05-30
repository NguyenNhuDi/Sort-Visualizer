import argparse
from utils import *
from sys import exit
from bogo_sort import *
from bubble_sort import *
from merge_sort import *
from quick_sort import *
from radix_sort import *
import constants

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='Sort Visualizer',
        description='Visualizes various sorting algorithms',
        epilog='Author: Di Nguyen '
    )

    parser.add_argument('-e', '--elements', type=int, required=False, default=constants.global_s_width / 2,
                        help='The number of elements '
                             'to sort ('
                             'must be a divisor of screen width)')
    parser.add_argument('-s', '--sort_name', required=False, default='bogo', help='Sorting algorithm to visualize')

    parser.add_argument('-width', required=False, type=int, default=constants.global_s_width,
                        help='Set the width of the screen')

    parser.add_argument('-height', required=False, type=int, default=constants.global_s_height,
                        help='Set the height of the screen')

    parser.add_argument('-ls', action='store_true', default=False,
                        help='List all known sorts')

    args = parser.parse_args()

    known_sorts = {
        'bogo': bogoSort,
        'bubble': bubbleSort,
        'merge': mergeSort,
        'quick': quickSort,
        'radix': radixSort
    }

    if args.ls:
        print()
        print()
        print()

        msg = f'KNOWN SORTS'
        print(f'{msg:_^50}')

        for name in known_sorts:
            print(name)
        msg = f''
        print(f'{msg:_^50}')
        print()
        print()
        print()
        exit(0)

    s_width = args.width
    s_height = args.height

    sort_name = args.sort_name.lower()
    complexity = args.elements

    constants.global_n = complexity
    constants.global_s_width = s_width
    constants.global_s_height = s_height

    assert s_width % complexity == 0, f'elements ({complexity}) must be a divisor of screen width ({s_width})'
    assert sort_name in known_sorts, f'{sort_name} is not known --ls to view known sorts'

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((s_width, s_height))

    pygame.init()

    func = known_sorts[sort_name]
    bars = getBar(complexity, screen, clock)

    print(len(bars))

    func(bars=bars, s=screen, c=clock)
    assert_correct(bars, screen, clock)
    pause_screen()

    pygame.quit()
