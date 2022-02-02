

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
                wrapper_str += indent + f'{k}: {v}' + '\n'

        step = 0
        return wrapper_str

    result += wrapper(dic, 0)
    result += '}'

    print(result)

    return result
