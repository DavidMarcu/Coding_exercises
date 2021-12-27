from src.utils import log_error


class Submarine:
    FORWARD_COMMAND = 'forward'
    DOWN_COMMAND = 'down'
    UP_COMMAND = 'up'

    def __init__(self):
        self.__depth = 0
        self.__distance = 0

    def get_final_coordinates(self, command_list: list) -> tuple:
        for command in command_list:
            try:
                self.__delegate_command(command)
            except ValueError as err:
                log_error(str(err))

        return (self.__distance, self.__depth)

    def get_depth_multiplied_by_distance(self):
        return self.__depth * self.__distance

    def __delegate_command(self, command: tuple):
        comm = str(command[0]).lower()
        if comm == self.FORWARD_COMMAND:
            self.__move_forward_by(int(command[1]))
        elif comm == self.UP_COMMAND:
            self.__go_up_by(int(command[1]))
        elif comm == self.DOWN_COMMAND:
            self.__dive_by(int(command[1]))
        else:
            raise ValueError(
                "invalid command. Valid commands: 'up', 'down' and 'forward'")

    def __move_forward_by(self, dist: int):
        if dist < 0:
            raise ValueError("Only positive values allowed")
        self.__distance = self.__distance + dist

    def __dive_by(self, depth: int):
        if depth < 0:
            raise ValueError("Only positive values allowed")
        self.__depth = self.__depth + depth

    def __go_up_by(self, amount: int):
        if amount < 0:
            raise ValueError("Only positive values allowed")
        self.__depth = self.__depth - amount
        if self.__depth < 0:
            self.__depth = 0

    def reset(self):
        self.__depth = 0
        self.__distance = 0
