import math


# -----------------------------------------={ Fail system }=-------------------------------------- #


def check_input(message, expected_type):

    if expected_type in (None, type, bool, int, float, tuple, list, dict):
        try:
            return expected_type(message)
        except:
            pass

    elif expected_type == str:
        raise Exception("Don't check for type str, just string it.")

    else:
        try:
            if isinstance(message, expected_type):
                return message

        except:
            pass

    raise TypeError(f'{message} must be of type {expected_type}, not {type(message)}.')


def check_vector2(vector, contain_type):
    new_vector = check_input(vector, tuple)
    if new_vector is not False:
        tester_x = check_input(new_vector[0], contain_type)
        tester_y = check_input(new_vector[1], contain_type)
        if tester_x is not False and tester_y is not False:
            return new_vector

    return False


def check_vector(vector, contains_type):
    new_vector = check_input(vector, tuple)
    new_vector1 = check_input(vector, list)
    good = True
    if new_vector is not False or new_vector1 is not False:
        for contains in new_vector:
            new_contains = check_input(contains, contains_type)
            if new_contains is False:
                good = False

    if good:
        return new_vector
    else:
        return False


# -------------------------------------={ Vector Manipulation }=---------------------------------- #

def add_vectors(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]


def angle_magnitude_to_vector(magnitude, direction):
    y_component = magnitude * math.cos(direction)
    x_component = magnitude * math.sin(direction)

    return x_component, y_component
