from src.day1 import SonarSweep

def read_from_file(filepath: str) -> list:
    input_as_list = []
    with open(filepath, "r") as file:
        for line in file:
            input_element = int(line)
            input_as_list.append(input_element)
    return input_as_list


if __name__ == '__main__':
    input_list = read_from_file('res/day1_1.txt')
    increase = SonarSweep.get_3_measurements_increase(input_list)
    print(increase)
