from gendiff.scripts.gendiff_main import generate_diff


test1_1 = 'tests/fixtures/file1.json'
test1_2 = 'tests/fixtures/file2.json'


def test_plain_fun():
    with open(
        'tests/fixtures/right_result_plain.txt', 'r') as right_result1_file:
        right_result1 = right_result1_file.read()
        assert generate_diff(test1_1, test1_2, 'plain') == right_result1[:-1]
