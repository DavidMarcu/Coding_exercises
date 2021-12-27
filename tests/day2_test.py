import unittest
from parameterized import parameterized

from src.day2 import Submarine


class SubmarineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Submarine()

    @parameterized.expand([
        ([('forward', 5), ('down', 3), ('up', 1)], (5, 2)),
        ([], (0, 0))
    ])
    def test_part1_happy_case(self, commands, expected):
        self.assertEqual(self.target.get_final_coordinates(commands), expected)
    
    
    @parameterized.expand([
        ([('right', 5)], (0, 0)),
        ([('right', 5), ('forward', 5), ('down', 3), ('', 1)], (5, 3))
    ])
    def test_part1_non_valid_commands_should_keep_the_result_unchanged(self, commands, expected):
        self.assertEqual(self.target.get_final_coordinates(commands), expected)
    

    @parameterized.expand([
        ([('dOwN', 5)], (0, 5)),
        ([('FORWARD', 5), ('foRward', 5), ('dOWn', 3), ('Up', 1)], (10, 2))
    ])
    def test_part1_right_command_but_with_wrong_capitalisation_should_do_the_commands(self, commands, expected):
        self.assertEqual(self.target.get_final_coordinates(commands), expected)

    
    @parameterized.expand([
        ([('up', 5)], (0, 0)),
        ([('forward', 5), ('down', 3), ('up', 5)], (5, 0))
    ])
    def test_part1_depth_cannot_be_below_0(self, commands, expected):
        self.assertEqual(self.target.get_final_coordinates(commands), expected)

    @parameterized.expand([
        ([('up', -5)], (0, 0)),
        ([('forward', 5), ('down', 3), ('up', -5), ('forward', -5)], (5, 3))
    ])
    def test_part1_commands_with_negative_values_should_not_change_the_result(self, commands, expected):
        self.assertEqual(self.target.get_final_coordinates(commands), expected)
    

if __name__ == '__main__':
    unittest.main()
