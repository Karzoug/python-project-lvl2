import yaml


def generate_diff_yaml(file1, file2):

    yml1 = yaml.load(open(file1))
    yml2 = yaml.load(open(file2))
    yml1 = {k: v for k, v in sorted(yml1.items(), key=lambda x: x[0])}
    yml2 = {k: v for k, v in sorted(yml2.items(), key=lambda x: x[0])}

    result = '{\n'

    for line1 in yml1:

        if line1 in yml2:

            if yml1[line1] == yml2[line1]:
                result += f'    {line1}: {yml1[line1]}\n'
            else:
                result += f'  - {line1}: {yml1[line1]}\n'
                result += f'  + {line1}: {yml2[line1]}\n'
        else:
            result += f'  - {line1}: {yml1[line1]}\n'

    for line2 in yml2:
        if line2 not in yml1:
            result += f'  + {line2}: {yml2[line2]}\n'

    result += '}'

    # print('right from func', result)
    return result
