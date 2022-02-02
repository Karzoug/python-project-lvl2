import argparse
from .generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')

    # parser.add_argument('string', metavar='first_line',
    #                     help='', default='')
    # parser.add_argument('string', metavar='second_line',
    #                     help='', default='')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(args)

    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    generate_diff(file1, file2)


if __name__ == '__main__':

    # main()
    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'
    generate_diff(file1, file2)
