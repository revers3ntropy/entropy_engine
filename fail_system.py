import global_data


# ================================================================================================
#  fail -- called when a fail is detected
#
#      Prints a report of the test which failed.
#
#  INPUT:  self
#
#          message - the message which is printed, a description of the failure
#
#  RETURNS:  none
#
#  CREATED: 2/8/20
#
# ================================================================================================
def error(message, location):
    if global_data.go:  # only prints once
        global_data.go = False  # prevents the main loop from running
        print('\n\n:-- Entropy Engine error --:\n')
        print('Error report:')

    print('    traceback: ' + location)
    print('    message: ' + message)
    print()
