from gendiff.scripts.stylish_formatter.stylish import stylish


def write_to_json(dic):

    result = stylish(dic)

    with open('tests/fixtures/result_json.json', 'w') as result_file:
        result_file.write(result)

    return result
