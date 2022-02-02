from gendiff.scripts.generate_diff import generate_diff


test1 = 'tests/fixtures/file1.yaml'
test2 = 'tests/fixtures/file2.yaml'


with open(
    'tests/fixtures/right_result_yaml.txt', 'r') as right_result1_file:
    right_result1 = right_result1_file.read()
    print('right from file:', right_result1[:-1])
    assert generate_diff(test1, test2) == right_result1[:-1]
