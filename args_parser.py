import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('queries',
                        type=str,
                        nargs='+',
                        help='queries')
    parser.add_argument(
        '-i',
        type=str,
        help='Type of intervals. Default - "day"',
        choices=['day', 'week', 'month'],
        default='day'
    )

    parser.add_argument(
        '-n',
        type=int,
        help='Number of intervals to search. Default - "7"',
        choices=range(1, 13),
        default=7
    )

    args = parser.parse_args()
    return args
