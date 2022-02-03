from gendiff.scripts.gendiff_main import generate_diff
# from gendiff.scripts.plain_formatter.plain import plain

test1_1 = 'tests/fixtures/file1.json'
test1_2 = 'tests/fixtures/file2.json'
# test2_1 = 'tests/fixtures/test2_1.json'
# test2_2 = 'tests/fixtures/test2_2.json'


with open(
    'tests/fixtures/right_result_plain.txt', 'r') as right_result1_file:
    right_result1 = right_result1_file.read()
    # print('right from file:', right_result1[:-1])
    # print(right_result1[:-1])
    # print('---------------------')
    assert generate_diff(test1_1, test1_2, 'plain') == right_result1


# with open(
#     'tests/fixtures/right_result_test2.txt', 'r') as right_result2_file:
#     right_result2 = right_result2_file.read()
#     # print('right from file:', right_result2[:-1])
#     assert generate_diff(test2_1, test2_2) == right_result2[:-1]
