import fail_system
import colour
import math


def add_vectors(v1, v2):
    v3 = [v1[0] + v2[0], v1[1] + v2[1]]
    return v3


def check_input(message, expected_type, fail):
    try:
        return expected_type(message)
    except:
        fail_system.error(fail[0], fail[1] + ', utilities.check_input (8)')
        return False


def check_vector2(vector, contain_type, location):
    new_vector = check_input(vector, tuple, (f'Force must be of type tuple, not {type(vector)}', location + ', utilities.check_vector2 (1)'))
    if new_vector is not False:
        tester_x = check_input(new_vector[0], contain_type, (f'Force must contain type float, not {type(vector[0])}', location + ', utilities.check_vector2 (3)'))
        tester_y = check_input(new_vector[1], contain_type, (f'Force must contain type float, not {type(vector[1])}', location + ', utilities.check_vector2 (4)'))
        if tester_x is not False and tester_y is not False:
            return new_vector

    return False


def create_colour(colour_):
    return colour.Colour(colour_[0], colour_[1], colour_[2])


def angle_magnitude_to_vector(magnitude, direction):
    y_component = magnitude * math.cos(direction)
    x_component = magnitude * math.sin(direction)

    return x_component, y_component
