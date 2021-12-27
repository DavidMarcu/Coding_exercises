import re
from src.day2 import Submarine
import src.utils as Utils

def read_from_file(filepath: str, elemnet_func) -> list:
    input_as_list = []
    with open(filepath, "r") as file:
        for line in file:
            input_element = elemnet_func(line)
            input_as_list.append(input_element)
    return input_as_list


if __name__ == '__main__':
    input_list = read_from_file('res/day2_1.txt', Utils.element_as_tuple)
    submarine = Submarine()
    final_coordintates = submarine.get_final_coordinates(input_list)
    print(final_coordintates)
    final_result = submarine.get_depth_multiplied_by_distance()
    print(final_result)
