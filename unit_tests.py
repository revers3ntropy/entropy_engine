import global_data

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : my_projects_name
#
#                                     File Name : unit_tests.py
#
#                                       Created : August 05, 2020
#
#                                   Last Update : August 00, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                 Tests functions in the program
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
#  global_data
#
# ------------------------------------------------------------------------------------------------
#
# class 'Tests' functions:
#  __init__          - contains the tests, test reports and the number of tests
#  fail              - prints an fail report
#  print_fail_report - prints the number of fails
#  run_all_tests     - runs all tests in all_tests
#
#  tester_tester     - tests the tester
#
# ================================================================================================


class Tests:

    # ================================================================================================
    #  __init__ -- sets the number of fails the tests which should be run.
    #
    #      Sets the int number_of_fails, and the list all_tests, which contains a tuple for every
    #      test to be run, which contains two strings: the first is the name of the function to run
    #      the test, the second the message to be displayed if the test fails.
    #
    #  INPUT:  self
    #
    #  RETURNS:  none
    #
    #  CREATED: 25/6/20
    #
    # ================================================================================================
    def __init__(self):
        self.number_of_fails = 0
        self.all_tests = [
            ('tester_tester', 'Tester failed'),
        ]

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
    #  CREATED: 25/6/20
    #
    # ================================================================================================
    def fail(self, message):
        if self.number_of_fails == 0:  # only prints once
            print()
            print()
            print(':-- Program failure --:')
            print()
            print('Error report:')

        print('    ' + message)
        global_data.go = False             # prevents the main loop from running
        self.number_of_fails += 1

    # ============================================================================================
    #  print_fail_report -- prints the number of fails
    #
    #  INPUT:  self
    #
    #  RETURNS:  none
    #
    #  CREATED: 25/6/20
    #
    # ============================================================================================
    def print_fail_report(self):
        print()                                             # new line for aesthetics
        if self.number_of_fails > 1:
            print(str(self.number_of_fails) + ' tests failed')
        elif self.number_of_fails == 1:
            print('1 test failed')
        elif self.number_of_fails == 0:
            print('No tests failed')
        else:
            print('An error has occurred: the number of program errors is ' +   # if an error occurs
                  str(self.number_of_fails) + ' which is out of bounds')

    # ============================================================================================
    #  run_all_tests -- loops through the tests and runs them
    #
    #       Loops through everything in self.all_tests, which contains details about all the
    #       tests. For each test, it runs the function, and if the function returns False then
    #       it treats it as an error. Once it has finished, it will print the number of tests
    #       which have failed.
    #
    #  INPUT:  self
    #
    #  RETURNS:  none
    #
    #  CREATED: 25/6/20
    #
    # ============================================================================================
    def run_all_tests(self):
        for test in self.all_tests:
            # runs the function who's name is found in test[0], and checks if its false or not
            if getattr(self, test[0])() is False:
                self.fail(test[1])

        self.print_fail_report()

    # ============================================================================================
    #  tester_tester -- tests the tester
    #
    #      Returns true regardless, meaning that if there is an error with the tester, then it
    #      gets picked up on before testing anything else.
    #
    #  INPUT:  self
    #
    #  RETURNS:  True
    #
    #  CREATED: 25/6/20
    #
    # ============================================================================================
    def tester_tester(self):
        return True
