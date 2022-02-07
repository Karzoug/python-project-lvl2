import json


def write_to_json(dic):

    replace = {
        'True': True,
        'False': False,
        'None': None
    }

    def wrap(in_dict):

        for k, v in in_dict.items():

            if isinstance(v, dict):
                in_dict[k] = wrap(v)
            elif v in replace:
                in_dict[k] = replace[v]
            # elif isinstance(v, bool):
            #     print(k, v)
            else:
                in_dict[k] = v
        return in_dict

    # print('dict before', dic)
    dic = wrap(dic)
    # print('hello:!', dic)
    result = json.dumps(dic, sort_keys=True, indent=4)
    # print(result)

    with open('tests/fixtures/result_json.json', 'w') as result_file:
        result_file.write(result)

    return result
