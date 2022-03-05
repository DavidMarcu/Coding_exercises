import unittest
from parameterized import parameterized
from adventOfCode2021.src.day1 import SonarSweep


class SonarSweepTest(unittest.TestCase):
  
    @parameterized.expand([
        ([199, 200], 1),
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
        ([199], 0),
        ([200, 199, 198, 197], 0),
        ([], 0)
    ])
    def test_part1(self, measurements, expected):
        self.assertEqual(SonarSweep.get_depth_increase(measurements), expected)

    @parameterized.expand([
        ([199, 200, 201, 202], 1),
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5),
        ([199], 0),
        ([199, 200, 201], 0),
        ([202, 201, 200, 199], 0),
        ([], 0)
    ])
    def test_part2(self, measurements, expected):
        self.assertEqual(SonarSweep.get_3_measurements_increase(measurements), expected)


if __name__ == '__main__':
    unittest.main()
