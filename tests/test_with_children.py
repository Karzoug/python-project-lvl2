from gendiff.scripts.generate_diff import generate_diff


test1_1 = 'tests/fixtures/file1.yaml'
test1_2 = 'tests/fixtures/file2.yaml'
test2_1 = 'tests/fixtures/file1.json'
test2_2 = 'tests/fixtures/file2.json'


def test_fun():

    with open(
        'tests/fixtures/right_result.txt', 'r') as right_result1_file:
        right_result1 = right_result1_file.read()
        assert generate_diff(test1_1, test1_2) == right_result1[:-1]

    with open(
        'tests/fixtures/right_result.txt', 'r') as right_result1_file:
        right_result1 = right_result1_file.read()
        assert generate_diff(test2_1, test2_2) == right_result1[:-1]
