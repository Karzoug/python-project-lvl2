import json
import yaml
from .stylish_formatter.stylish import stylish
from .plain_formatter.plain import plain
from .json_formatter.json_format import write_to_json


def sort_dict(dict_in):

    if isinstance(dict_in, dict):

        new_dict = {}

        for k, v in sorted(dict_in.items(), key = lambda x: x[0]):
            new_dict['    ' + k] = sort_dict(v)

    else:
        new_dict = str(dict_in)

    return new_dict


# flake8: noqa: C901
def generate_diff(file1, file2, format='stylish'):

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

            try:
                type1 = isinstance(str1[line], dict)
            except KeyError:
                type1 = None

            try:
                type2 = isinstance(str2[line], dict)
            except KeyError:
                type2 = None
            
            if type1 == False: 
                str1[line] = str(str1[line])

            if type2 == False: 
                str2[line] = str(str2[line])

            if line in str1 and line in str2:

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

    if format == 'plain':
        # print(plain(result))
        return plain(result)
    elif format == 'json':
        # print(write_to_json(result))
        return write_to_json(result)
    else:
        # print(stylish(result))
        return stylish(result)