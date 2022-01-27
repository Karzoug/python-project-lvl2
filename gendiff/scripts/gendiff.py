import argparse
import json
import os

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
    file1 = os.path.join('', file1)
    file2 = os.path.join('', file2)

    js1 = json.load(open(file1))
    js2 = json.load(open(file2))
    js1 = {k: v for k,v in sorted(js1.items(), key=lambda x: x[0])}
    js2 = {k: v for k,v in sorted(js2.items(), key=lambda x: x[0])}
    print(js1, js2)

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
        if not line2 in js1:
            result += f'  + {line2}: {js2[line2]}\n'

    result += '}'

    print(result)


if __name__ == '__main__':

    # main()
    generate_diff('file1.json', 'file2.json')