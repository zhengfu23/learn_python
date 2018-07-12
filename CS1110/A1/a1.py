# a1.py
# PUT YOUR NAME(S) AND NETID(S) HERE
# Sources/people consulted: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
# Skeleton by Prof. Lee (cs1110-prof@cornell.edu), Feb 14 2018

"""
Functions for finding whether a class is open or closed on a roster.

We use "backwards single quotes" --- like this: `hi there` --- in the
docstrings below to visually set off variable names.
"""


# Helper function
def before_first_double_quote(text):
    """Returns: the part of string `text` right up to but not including
    the first double-quote.

    Precondition: string `text` contains at least one double-quote.

    Example: before_first_double_quote('abd"def') returns the string
        abd
    """
    return text[:text.find('"')]


# Helper function
def after(tag, text):
    """Returns: all of string `text` that occurs just after the first
    occurrence of string `tag` in `text`.

    Preconditions:
        `text` [str] contains an instance of `tag`
        `tag` [str] has length > 0

    Example: if `tag` is the string
        <a id="c111">
    and `s` is the string
        start <a id="c111">xthis that the other
    then this functions returns the string
         xthis that the other
    """
    return text[text.find(tag)+len(tag):]


def open_status(class_num, data):
    """Returns the open-ness status of class `class_num` according to `data`.

    `class_num`: string version of a class number, e.g., "10776" at Cornell.

    `data`: a string whose preconditions are easiest explained by example.
        Suppose `class_num` is "10775".
        Then, `data` must contain somewhere within it a single occurrence of
           <a id="c10775">
        and this is followed by text where the first occurrence of the string
            open-status-
        (the ending hyphen is important) is one of
            open-status-open"
        or
            open-status-closed"
        or any string of the form
            open-status-???"
        (the ending double-quote is important to notice)
        where the ??? stands for a sequence of characters not containing quotes
        that represents the open-ness status of the course. (For example, maybe
        there is such a thing as open-status-waitlist")

    This function returns whatever ??? is.

    Example: if `class_num` is "10775", and `data` is the string
        <a id="c10775"> fa-circle open-status-open"></i></span>
    then this function returns the string
        open

    Example: if `class_num` is "10775", and `data` is the string
        dum dee dum <a id="c10775"> open-stat open-status-CLOSED" tral la la
    then this function returns the string
        CLOSED

    Example: if `class_num` is "432" and `data` is the string
        <a id="c4321"> ha open-status-open" <a id="c432"> open-status-never!""
    then this function returns the string
        never!
    (The exclamation point must be included.)

    Example: if `class_num` is "432" and `data` is the string
        <a  id="c432"> ho open-status-open" <a id="c432"> open-status-nope."
    then this function returns the string
        nope.
    (The number of spaces matters between the `a` and the `id` matters.)



    """
    # STUDENTS: YOUR IMPLEMENTATION MUST CALL AND MAKE USE OF THE RETURN
    # VALUE OF helper functions `after` and `before_first_double_quote`
    # (or new helper functions you write that call them).

    # HINT for how to find where to begin searching in the string.
    # It might not work to run data.index("10775") to find the location
    # of '<a id="c10775">' in data.  (See test case 2 in
    # a1test.test_open_status to see why not.)
    # But the following is a legal expression:
    #   data.index('<a id="c' + "10775" + '">')
    # as is
    #   data.index("<a id=\"c" + "10775" + "\">")
    # Can you adapt either idea to your situation?
    a_tag = "<a id=\"c" + class_num + "\">"
    status = before_first_double_quote(after("open-status-", after(a_tag, data)))
    return status


def label(class_num, data):
    """Returns, as a single string,  the common name, component and component
    number for class `class_num` according to `data`.

    `class_num`: string version of a class number, e.g., "10776" at Cornell.

    `data`: a string whose preconditions are easiest explained by example.
        Suppose `class_num` is "10782".
        Then, `data` matches the pattern
             ... <a id="c10782"> ... class="course-repeater">CS 1110&nbsp;...
            data-ssr-component="DIS" data-section="208"
        And the function should return the string
            CS 1110 DIS 208
        with no beginning or trailing whitespace.

        That is, `data` must contain somewhere within it a single occurrence of
            <a id="c10782">
        and this is followed by text where the first occurrence of the string
            class="course-repeater">
        (the ending quote and angle-bracket is important) is followed by the
        common name of the course, and then the string
            &nbsp;
        and the first occurrence of the string
            data-ssr-component="
        is followed by the component, followed by a double-quote,
        and the first occurrence of the string
            data-section="
        is followed by the component number followed by a double-quote.

        The function returns the string formed by concatenating the common
        name, then a space, then the component, then a space, then the
        component number.

    """
    # STUDENTS: YOUR IMPLEMENTATION MUST CALL AND MAKE USE OF THE RETURN
    # VALUE OF helper functions `after` and `before_first_double_quote`
    # (or new helper functions you write that call them).

    # HINT: You may find it easier to develop this function incrementally,
    # That is, consider the following outline.
    # 1. Just get the function to store the common name in a variable.
    # 2. Once that's working, get it to store the component in another variable.
    # 3. Then, get it to store the component number in a third variable.
    # 4. Figure out how to combine the values of the three variables to
    #    get the desired return value
    a_tag = "<a id=\"c" + class_num + "\">"
    info_string = after(a_tag, data)
    class_name = after("class=\"course-repeater\">", info_string)[:len("CS 1110")]
    info_string = after("data-ssr-component=\"", info_string)
    ssr_component = before_first_double_quote(info_string)
    section_number = before_first_double_quote(after("data-section=\"", info_string))
    return class_name + " " + ssr_component + " " + section_number


