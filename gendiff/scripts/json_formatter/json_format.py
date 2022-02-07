from gendiff.scripts.stylish_formatter.stylish import stylish
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
            elif isinstance(v, int):
                in_dict[k] = int(v)
        return in_dict

    dic = wrap(dic)
    # print(dic)
    result = json.dumps(dic, sort_keys=True, indent=4)
    print(result)

    with open('tests/fixtures/result_json.json', 'w') as result_file:
        result_file.write(result)

    return result
