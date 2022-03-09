import unittest
from parameterized import parameterized
from codeForces.src.petya_and_exam import is_valid_query, get_input, solve_queries

class PetyaAndExamTest(unittest.TestCase):

    COMMON_PATH = 'codeForces/res/Petya_and_exam'

    @parameterized.expand([
        ('ab', 'a?a', 'aaa'),
        ('abc', 'a?a?a*', 'abaca'),
        ('abc', 'a?a?a*', 'aaaaax'),
        ('a', 'a?', 'aa'),
        ('a', '*a?', 'aa'),
        ('a', '*a?', 'xaa'),
        ('a', 'a*?', 'axa'),
        ('adz', 'a*adz?', 'ayadzz'),
        ('adz', 'a*adz?', 'ayyadzz'),
        ('adz', 'a*adz?', 'ayybbadzz'),
        ('adz', 'a*adz', 'aadz')
    ])
    def test_query_is_valid(self, valid_letters, pattern, query):
        self.assertTrue(is_valid_query(valid_letters, pattern, query))

    
    @parameterized.expand([
        ('ab', 'a?a', 'aab'),
        ('abc', 'a?a?a*', 'abacaba'),
        ('abc', 'a?a?a*', 'apapa'),
        ('adz', 'a*adz?', 'ayyabbadzz'),
        ('a', 'a?', 'a'),
    ])
    def test_query_is_not_valid(self, valid_letters, pattern, query):
        self.assertFalse(is_valid_query(valid_letters, pattern, query))


    @parameterized.expand([
        (f'{COMMON_PATH}/testcase1.txt', f'{COMMON_PATH}/output_testcase1.txt', f'{COMMON_PATH}/output_testcase1_result.txt'),
        (f'{COMMON_PATH}/testcase2.txt', f'{COMMON_PATH}/output_testcase2.txt', f'{COMMON_PATH}/output_testcase2_result.txt')
    ])
    def test_solve_queries_work(self, input_file, output_file, output_result):
        input_tuple = get_input(input_file)
        solve_queries(valid_letters=input_tuple[0], pattern=input_tuple[1],
        no_of_queries=input_tuple[2], queries=input_tuple[3], output=output_result)
        with open(output_file) as expected:
            with open(output_result) as result:
                for expected_line, result_line in zip(expected.readlines(), result.readlines()):
                    self.assertEqual(expected_line, result_line, f'expected: {expected_line} != result: {result_line}')



if __name__ == '__main__':
    unittest.main()
