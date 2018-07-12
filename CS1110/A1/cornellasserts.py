# cornellasserts.py
# Walker M. White (wmw2), Lillian Lee (LJL2), Steve Marschner (srm2)
# Feb 10, 2018

"""Support functions for testing.

This module provides function-level testing tools.  It is a replacement
for  the built-in Python package `unittest`, which is less user-friendly
and requires an understanding of object-oriented programming.

This module's "assert-style" functions are different from standard `assert`
statements. They stop execution of Python and report the location of the
error.
"""


import numpy
import traceback  # for examining the call stack
from sys import exit


def quit_with_error(msg):
    """Quit Python, after printing error message `msg` [str], location, and
    termination message `Quitting with Error`.

    Precondition: called within another function (technically, the call stack
    must have depth at least 3.)
    """

    stack = traceback.extract_stack()
    frame = stack[-3]
    print(msg)
    if (frame[3] is None):
        suffix = ''
    else:
        suffix = ": " + frame[3]
    print('Line ' + repr(frame[1]) + ' of ' + frame[0] + suffix)
    print('Quitting with Error')
    exit()


def assert_equals(expected, received):
    """Quit if `expected` and `received` differ (!=), printing some info.
       Does nothing otherwise.

    `expected` should be an expected value for a test.
    `received` should be (the value of) an expression representing a test.

    Precondition:  `expected` and `received` are not both floats. (For that
    use case, use assert_floats_equal().)

    Example usage:
        assert_equals(10, my_function(14))
    If `my_function(14)` is "Aye, me", the printout is:
        assert_equals: expected 10 but instead got 'Aye, me'
        Line <corresponding line number> of <relevant file>
        Quitting with Error
    If `my_function(14)` is 35.2, the printout is:
        assert_equals: expected 10 but instead got 35.2
        Line <corresponding line number> of <corresponding file>
        Quitting with Error


    The meaning of "differ" for this function is !=.
    """
    if (expected != received):
        message = 'assert_equals: expected ' + \
            repr(expected) + ' but instead got ' + repr(received)
        quit_with_error(message)


def assert_not_equals(expected, received):
    """Quit if `expected` and `received` are the same (==), printing some info.
       Does nothing otherwise.

    `expected` should be an expected value for a test.
    `received` should be (the value of) an expression representing a test.

    Precondition:  `expected` and `received` are not both floats. (For that
    use case, use assert_floats_not_equal().)

    Example usage:
        assert_not_equals(10, my_function(14))
    If `my_function(14)` is 10, the printout is:
        assert_not_equals: expected something different from 10; got 10
        Line <relevant line number> of <relevant file>:
        Quitting with Error
    """
    if (expected == received):
        message = 'assert_not_equals: expected something different from ' + \
            repr(expected) + '; got ' + repr(received)
        quit_with_error(message)


def assert_true(received):
    """Quit if `received` is False, printing an error message.
       Does nothing otherwise.

    `received` should be (the value of) an expression representing a bool.

    Example usage:
        assert_true(2+2==5)
    The output is:
        assert_true: expected True but instead got False
        Line <relevant line number>  of <relevant file>:
        Quitting with Error

    """
    if (not received):
        msg = "assert_true: expected True but instead got False"
        quit_with_error(msg)


def assert_false(received):
    """Quit AssertionError if received is True, printing an error message.
       Does nothing otherwise.

    `received` should be (the value of) an expression representing a bool.

    Example usage:
        cornelltest.assert_false(2+2==4)
    Output:
        assert_false: expected False but instead got True
        Line <relevant line number>  of <relevant file>:
        Quitting with Error
    """
    if (received):
        msg = "assert_false: expected False but instead got True"
        quit_with_error(msg)


def assert_floats_equal(expected, received):
    """Quit if floats/ints `expected` and `received` differ, printing an
    error message.
    If one of the arguments is not a number, quits with another error message.
    Does nothing otherwise.
    Preconditions:
        `expected` is either a float or an int
        `received` is either a float or an int

    `expected` should be an expected value for a test.
    `received` should be (the value of) an expression representing a test.

    "differ" here means in the sense of the `allclose` function in the
    numerical computation package ``numpy``, which has a built-in (small) level
    of tolerance in the relative difference between float numbers.


    If either argument is not a number, the function quits with a message
    referring to the first non-number argument. Example:
        assert_floats_equal("alas", 4.5)
    gives output
        assert_floats_equal: first argument 'alas' is not a number
        Line <relevant line number> of <relevant file>:
        Quitting with Error
    """
    number = [float, int]  # list of number types
    if type(expected) not in number:
        msg = ("assert_floats_equal: " +
               "first argument " + repr(expected) + " is not a number")
        quit_with_error(msg)

    if type(received) not in number:
        msg = ("assert_floats_equal: " +
               "second argument " + repr(received) + " is not a number")
        quit_with_error(msg)

    if not numpy.allclose([expected], [received]):
        msg = ("assert_floats_equal: expected " + repr(expected) +
               " but instead got " + repr(received))
        quit_with_error(msg)
