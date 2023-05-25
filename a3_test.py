# a3_test.py
# Prof. Bracy, AWB93
# Mar 10, 2023

import cornellasserts as ca
import inspect  # to print the name of a (test) function that is running

import a3_helper

# helper written by Prof. Lee, LJL2
def print_testing(start_or_end):
    """If start_or_end is 'start',
        print message about starting function that called this function
       If start_or_end is 'end'
        print message about ending function that called this function

    Precondition: start_or_end is either 'start' or 'end'"""
    caller = inspect.currentframe().f_back.f_code.co_name
    if start_or_end == 'start':
        print("Starting " + caller)
    elif start_or_end == 'end':
        print(caller + " seems to have passed (didn't crash/stop mid-way).")
        print("\n")

# ---------------------------------------------------------
# Test code for your 7 functions are below.
# Note: not all tests are exhuastive.
#    You are encouaged to add more test cases.
# ---------------------------------------------------------

# STUDENTS: these tests are not exhaustive!
def test_remove_numerics():
    print_testing('start')

    # Testing whether we remove the numerics
    ca.assert_equals("abc", a3_helper.remove_numerics("6a2b3c1"))

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_remove_multiple_spaces():
    print_testing('start')

    # Testing whether we remove the occurence of multiple spaces
    ca.assert_equals(" a b c", a3_helper.remove_multiple_spaces("  a  b  c"))

    print_testing('end')

def test_initialize_counts():
    print_testing('start')

    d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0,
    'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
    ' ': 0}
    ca.assert_equals(d, a3_helper.initialize_counts())

    print_testing('end')

def test_apply_mapping():
    print_testing('start')
    d1 = {'a':'e', 'b':'c', 'c':'d', 'd':'a', 'e':'f', 'f':'b', 'g':'g'}
    ca.assert_equals("ecdafbg", a3_helper.apply_mapping("abcdefg", d1))

    d2 = {'a': 'xx', 'b': 'yy', 'c': 'wow'}
    ca.assert_equals("yywowxxyy", a3_helper.apply_mapping("bcab", d2))

    d3 = {' ': 'z', 'b': 'y', '!': ']'}
    ca.assert_equals("y]z", a3_helper.apply_mapping("b! ", d3))

    print_testing('end')

def test_make_dict_from_lists():
    print_testing('start')

    ca.assert_equals({1:5, 2:6, 3:7, 4:8},
        a3_helper.make_dict_from_lists([1,2,3,4],[5,6,7,8]))
    ca.assert_equals({"a":5, "b":6, "c":7, "d":8},
        a3_helper.make_dict_from_lists(["a","b","c","d"],[5,6,7,8]))

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_get_letter_counts():
    print_testing('start')

    d = {'a': 3, 'b': 3, 'c': 2, 'd': 1, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0,
    'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
    ' ': 3}
    ca.assert_equals(d, a3_helper.get_letter_counts("ab abc acb d"))
    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_get_pair_counts():
    print_testing('start')
    d = {'ab':2, 'ac':1, 'bc':1, 'cb':1, 'b ':1, 'c ':1, ' a':2}
    ca.assert_equals(d, a3_helper.get_pair_counts("ab abc acb"))
    print_testing('end')

if __name__ == '__main__':

    test_remove_numerics()
    test_remove_multiple_spaces()
    test_initialize_counts()
    test_apply_mapping()
    test_make_dict_from_lists()
    test_get_letter_counts()
    test_get_pair_counts()
