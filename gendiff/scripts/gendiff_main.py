import argparse
from .generate_diff import generate_diff
import os


def main():
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('first_line')
    parser.add_argument('second_line')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')

    args = parser.parse_args()

    file1 = vars(args)['first_line']
    file2 = vars(args)['second_line']
    formatter = vars(args)['format']

    if not file1.startswith('tests'):
        file1 = os.path.join('tests', 'fixtures', file1)
    if not file2.startswith('tests'):
        file2 = os.path.join('tests', 'fixtures', file2)

    generate_diff(file1, file2, formatter)


if __name__ == '__main__':

    main()

