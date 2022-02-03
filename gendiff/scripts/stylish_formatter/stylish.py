def to_str(val):
    replace = {
        'False': 'false',
        'True': 'true',
        'None': 'null'
    }
    if str(val) in replace:
        return replace[val]
    else:
        return val


def stylish(dic):

    result = '{\n'

    def wrapper(nest_dict, step):

        wrapper_str = ''
        # print(nest_dict, type(nest_dict))

        for k, v in nest_dict.items():

            indent = '    ' * step

            if isinstance(v, dict):

                wrapper_str = wrapper_str + indent + k + ': {\n'
                wrapper_str += wrapper(v, step + 1) + indent + '    }\n'

            else:
                wrapper_str += indent + f'{k}: {to_str(v)}' + '\n'

        step = 0
        return wrapper_str

    result += wrapper(dic, 0)
    result += '}'

    # print('Stylish result:\n', result)

    return result
