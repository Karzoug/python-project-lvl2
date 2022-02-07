def way(name, path=''):

    name = name.replace('  - ', '').replace('  + ', '').replace('    ', '')

    if path:
        path = path.replace("'", '')
        return f"'{'.'.join([path, name])}'"
    else:
        return complex(name)


def complex(val):
    replace = {
        'False': 'false',
        'True': 'true',
        'None': 'null'
    }

    if isinstance(val, dict):
        return '[complex value]'
    elif str(val) in replace:
        return replace[val]
    elif val.isdigit():
        return val
    else:
        return f"'{val}'"


# flake8: noqa: C901
def plain(dic):

    result = ''

    def wrapper(nest_dic, path=''):

        wrapper_str = ''

        for k, v in nest_dic.items():

            type1 = isinstance(v, dict)
            new_path = f"{way(k, path)}"
            
            if k.startswith('    ') and type1:
                wrapper_str = wrapper_str + wrapper(v, new_path)

            # removed or updated
            elif k.startswith('  - '):

                if k.replace('  - ', '  + ') in nest_dic.keys():
                    # UPDATED
                    new_v = nest_dic[k.replace('  - ', '  + ')]
                    wrapper_str += f"Property {new_path} was updated. From "\
                                   f"{complex(v)} to {complex(new_v)}"+'\n'
                else:
                    # REMOVED
                    wrapper_str += f"Property {new_path} was removed\n"

            elif k.startswith('  + ') and not\
                 k.replace('  + ', '  - ') in nest_dic:
                 # ADDED
                wrapper_str += f"Property {new_path} was added with value:"\
                               f" {complex(v)}" + "\n"

        return wrapper_str

    result += wrapper(dic, '')
    result = result[:-1]

    return result


            


                