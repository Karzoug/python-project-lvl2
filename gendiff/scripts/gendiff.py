import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('string', metavar='first_line', nargs='+', help='', default='')
    parser.add_argument('string', metavar='second_line', nargs='+', help='', default='')

    args = parser.parse_args()


if __name__ == '__main__':

    main()

# positional arguments:
#   first_file
#   second_file

# optional arguments:
#   -h, --help            show this help message and exit
