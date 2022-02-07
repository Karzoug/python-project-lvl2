from gendiff.scripts.gendiff_main import generate_diff


test1_1 = 'tests/fixtures/file1.yaml'
test1_2 = 'tests/fixtures/file2.yaml'


def test_json_fun():

    with open('tests/fixtures/right_result.json', 'r') as right_result_file:
        right_result = right_result_file.read()

        generate_diff(test1_1, test1_2, 'json')

        with open('tests/fixtures/result_json.json', 'r') as result_file:
            result = result_file.read()
            print(len(right_result), len(result))
            assert result == right_result[:-1]
