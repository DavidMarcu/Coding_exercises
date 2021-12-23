class SonarSweep:
    def __init__(self):
        pass


    @staticmethod
    def _increment_if_increased(increase, previous_measurement, current_measurement):
        return increase + 1 if current_measurement > previous_measurement else increase


    @staticmethod
    def get_depth_increase(measurements: list):
        increase = 0
        for (previous_measurement, current_measurement) in zip(measurements[0::1], measurements[1::1]):
            increase = SonarSweep._increment_if_increased(increase, previous_measurement, current_measurement)
        return increase


    @staticmethod
    def get_3_measurements_increase(measurements: list):
        increase = 0
        measurements_size = len(measurements)
        if measurements_size < 3:
            return 0
        previous_measurement = sum(measurements[0:3])
        for current_index in range(1, measurements_size - 2):
            current_measurement = previous_measurement - measurements[current_index - 1] + measurements[current_index + 2]
            increase = SonarSweep._increment_if_increased(increase, previous_measurement, current_measurement)
            previous_measurement = current_measurement
        return increase 

