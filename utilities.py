import fail_system
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
        tester_x = check_input(new_vector[0], contain_type, (f'Force must contain type {contain_type}, not {type(vector[0])}', location + ', utilities.check_vector2 (3)'))
        tester_y = check_input(new_vector[1], contain_type, (f'Force must contain type {contain_type}, not {type(vector[1])}', location + ', utilities.check_vector2 (4)'))
        if tester_x is not False and tester_y is not False:
            return new_vector

    return False


def check_vector(vector, contains_type, location):
    new_vector = check_input(vector, tuple, (f'Force must be of type tuple, not {type(vector)}', location + ', utilities.check_vector2 (1)'))
    new_vector1 = check_input(vector, list, (f'Force must be of type tuple, not {type(vector)}', location + ', utilities.check_vector2 (1)'))
    good = True
    if new_vector is not False or new_vector1 is not False:
        for contains in new_vector:
            new_contains = check_input(contains, contains_type, (f'vector must contain type float, not {type(contains)}', location + ', utilities.check_vector2 (3)'))
            if new_contains is False:
                good = False

    if good:
        return new_vector
    else:
        return False


def angle_magnitude_to_vector(magnitude, direction):
    y_component = magnitude * math.cos(direction)
    x_component = magnitude * math.sin(direction)

    return x_component, y_component
