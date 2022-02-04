from gendiff.scripts.generate_diff import generate_diff


def test_yaml_fun():

    test1 = 'tests/fixtures/test1_1.yaml'
    test2 = 'tests/fixtures/test1_2.yaml'
    with open(
        'tests/fixtures/right_result_yaml.txt', 'r') as right_result1_file:
        right_result1 = right_result1_file.read()
        # print('right from file:', right_result1[:-1])
        assert generate_diff(test1, test2) == right_result1[:-1]
