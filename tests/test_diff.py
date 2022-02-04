from gendiff.scripts.gendiff_main import generate_diff


test1_1 = 'tests/fixtures/test1_1.json'
test1_2 = 'tests/fixtures/test1_2.json'
test2_1 = 'tests/fixtures/test2_1.json'
test2_2 = 'tests/fixtures/test2_2.json'

def test_diff_fun():
    with open(
        'tests/fixtures/right_result_test1.txt', 'r') as right_result1_file:
        right_result1 = right_result1_file.read()
        assert generate_diff(test1_1, test1_2) == right_result1[:-1]

    with open(
        'tests/fixtures/right_result_test2.txt', 'r') as right_result2_file:
        right_result2 = right_result2_file.read()
        assert generate_diff(test2_1, test2_2) == right_result2[:-1]
