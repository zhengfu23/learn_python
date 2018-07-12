# a1test.py
# PUT YOUR NAME(S) AND NETID(S) HERE
# Sources/people consulted: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
# Skeleton by Prof. Lee (cs1110-prof@cornell.edu), Feb 14 2018

""" Testing code for CS1110 A1, Spring 2018. """

import cornellasserts
import a1
import sys  # to allow early quit


def test_helper1():
    """Test function a1.before_first_double_quote"""
    print("Testing a1.before_first_double_quote")

    # 1st quote three in from beginning
    result = a1.before_first_double_quote('abd"def')
    cornellasserts.assert_equals('abd', result)

    # quote at beginning
    result = a1.before_first_double_quote('"def"')
    cornellasserts.assert_equals('', result)

    # STUDENTS: PUT AN ADEQUATE SET OF ADDITIONAL TESTCASES BELOW.
    # You should add at least two.



def test_helper2():
    """Test function a1.after"""
    print("Testing a1.after")

    # tag in the middle
    t = '<a id="c111">'
    s = 'start <a id="c111">xthis that the other'
    result = a1.after(t,s)
    cornellasserts.assert_equals('xthis that the other', result)

    # STUDENTS: PUT AN ADEQUATE SET OF ADDITIONAL TESTCASES BELOW
    # You should add at least two.



def test_open_status():
    """Test function a1.open_status"""

    print("Testing a1.open_status")

    # standard case
    d1 = '<a id="c10775"> fa-circle open-status-open"></i></span>'
    result = a1.open_status("10775", d1)
    cornellasserts.assert_equals("open", result)

    # a near-match at the beginning, so check for exact match
    d2 = '<a id="10775"> open-status-no <a id="c10775"> open-status-Y"></i></span>'
    result = a1.open_status("10775", d2)
    cornellasserts.assert_equals("Y", result)


    # STUDENTS: PUT AN ADEQUATE SET OF  ADDITIONAL TESTCASES BELOW
    # You should add at least two.



def test_label():
    """Test function a1.label"""

    print("Testing a1.label")

    # STUDENTS, we have constructed enough test cases for you, so
    # you don't need to add any more.  You're welcome.

    print(" running test case 1")
    s1 = 'blah blah blah <a id="c10782"> more stuff '
    s1 = s1 + 'class="course-repeater">CS 1110&nbsp;abcedfgh'
    s1 = s1 + 'data-ssr-component="DIS" data-section="208"789012'
    result = a1.label("10782", s1)
    cornellasserts.assert_equals("CS 1110 DIS 208", result)

    print(" running test case 2, has two courses in it and some tricky stuff")
    s2 = s1 + '<a id="c45">        class="course-repeater">ART 314&nbsp;    '
    s2 = s2 + 'data-ssr-component data-ssr-component="LEC"   '
    s2 = s2 + 'data-section=118 data-section="412"'
    result = a1.label("45",s2)
    cornellasserts.assert_equals("ART 314 LEC 412", result)


# STUDENTS: don't edit this function.
def ask_to_quit():
    """Ask if user wishes to keep testing, terminate execution if not."""
    msg = 'Press q to quit, anything else to start testing the next function. '
    response = input(msg)
    if response == "q":
        sys.exit()


###########
# Calls to testing functions
###########

test_helper1()
ask_to_quit()

test_helper2()
ask_to_quit()

test_open_status()
ask_to_quit()

test_label()
print('\n\nPassed all test functions for a1. Hurrah!')
