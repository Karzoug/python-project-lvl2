import json
import yaml
from .stylish import stylish


def sort_dict(dict_in):

    if isinstance(dict_in, dict):

        new_dict = {}

        for k, v in sorted(dict_in.items(), key = lambda x: x[0]):
            new_dict['    ' + k] = sort_dict(v)

    else:
        new_dict = dict_in

    return new_dict


# flake8: noqa: C901
def generate_diff(file1, file2):

    if file1.endswith('.json'):
        fil1 = json.load(open(file1))
        fil2 = json.load(open(file2))
    else:
        fil1 = yaml.load(open(file1), Loader=yaml.Loader)
        fil2 = yaml.load(open(file2), Loader=yaml.Loader)

    result = {}

    def find_diff(str1, str2):

        diff = {}

        # sort by keys alphabet
        all_set = sorted(set(str1).union(set(str2)))

        for line in all_set:
            
            if line == 'id':
                print('DEEEP!!!,fdfd')

            try:
                type1 = isinstance(str1[line], dict)
            except KeyError:
                type1 = None

            try:
                type2 = isinstance(str2[line], dict)
            except KeyError:
                type2 = None

            if line in str1 and line in str2 and type1 == type2:

                # both dict
                if type1 and type2:
                    diff['    ' + line] = find_diff(str1[line], str2[line])

                # both not dict and equal
                elif not type1 and not type2 and str1[line] == str2[line]:
                    diff['    ' + line] = sort_dict(str1[line])

                # if both in str1 and str2 and not equal
                else:
                    diff['  - ' + line] = sort_dict(str1[line])
                    diff['  + ' + line] = sort_dict(str2[line])

            elif line in str1:
                diff['  - ' + line] = sort_dict(str1[line])

            elif line in str2:
                diff['  + ' + line] = sort_dict(str2[line])

        return diff

    result = find_diff(fil1, fil2)

    # print(result)
    # print(stylish(result))

    return result
