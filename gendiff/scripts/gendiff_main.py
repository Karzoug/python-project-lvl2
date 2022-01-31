import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('string', metavar='first_line',
                        help='', default='')
    parser.add_argument('string', metavar='second_line',
                        help='', default='')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(args)


def generate_diff(file1, file2):
    print('hello')
    js1 = json.load(open(file1))
    js2 = json.load(open(file2))
    js1 = {k: v for k, v in sorted(js1.items(), key=lambda x: x[0])}
    js2 = {k: v for k, v in sorted(js2.items(), key=lambda x: x[0])}

    result = '{\n'

    for line1 in js1:

        if line1 in js2:

            if js1[line1] == js2[line1]:
                result += f'    {line1}: {js1[line1]}\n'
            else:
                result += f'  - {line1}: {js1[line1]}\n'
                result += f'  + {line1}: {js2[line1]}\n'
        else:
            result += f'  - {line1}: {js1[line1]}\n'

    for line2 in js2:
        if line2 not in js1:
            result += f'  + {line2}: {js2[line2]}\n'

    result += '}'

    # print('right from func', result)
    return result


if __name__ == '__main__':

    # main()
    file1 = 'gendiff/tests/fixtures/test1_1.json'
    file2 = 'gendiff/tests/fixtures/test1_2.json'
    generate_diff(file1, file2)
