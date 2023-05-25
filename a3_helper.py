# a3_helper.py
# "ebc68" and "mca74"
# Sources/people consulted: "TA: Minhaj Fahad"
# 3/17/2023
# Skeleton by Prof. Bracy, AWB93, Feb 10, 2023



import numpy as np
import math, re

alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z',' ']

np.random.seed(17)

""" The first 7 functions of this file are the functions students
    need to complete for A3.

    We have placed them in increasing difficulty so we recommend
    you start at the top of this file and work your way down.

    Have fun!

"""

# Fuction 1 for A3
def remove_numerics(text):
    """Returns: a copy of the string `text` with all numerics (0-9) removed

    Precondition: `text` is a str
    """
    # STUDENTS: your implementation must make effective use of for-loops.
    # the only string method you may use is isnumeric() (see writeup)
    # approach: loop over each character in the string, if it is a numeric,
    # DO NOT include it in the result.
    result = ''
    for x in text:
        if not x.isnumeric():
            result = result + x
             # this is not correct. Replace it with your work!
    return result

# Fuction 2 for A3
def remove_multiple_spaces(text):
    """Returns: a copy of the string `text` where any sequence of multiple
    spaces are replaced by a single space.

    Precondition: `text` is a str
    """
    result = ''
    count = 1
    for x in text:
        if count != len(text):
            if x + text[count] != '  ':
                result = result + x
                count = count + 1
            else:
                count = count + 1
        else:
            result = result + x


        # STUDENTS: your implementation must make effective use of for-loops.
    # approach: loop over each character in the string, if the character
    # is a space, only include it in the result if the previous character
    # was not also a space.
    # this is not correct. Replace it with your work!
    return result
# Fuction 3 for A3
def initialize_counts():
    """Returns: a dictionary whose keys are each of the characters in
    alpha_list and whose values are all 0.
    """
    dict = {}
    for x in alpha_list:
        item = {x: 0}
        dict.update(item)
    return dict

     # STUDENTS: your implementation must make effective use of for-loops.

# Fuction 4 for A3
def apply_mapping(text_seq, mapping):
    """Transforms the given text sequence `text_seq` using `mapping`

    Preconditions:
      `text_seq` can be either be a list of characters or a string
                 every character in `text_seq` is a key in `mapping`

      `mapping` is a dictionary whose keys are characters (string length 1)
                and whose values are strings

    Returns: the transformed text, a string
    """
    # For lack of a better placeholder, we just return the original text.
    # STUDENTS: replace this with your implementation!
    mapped_text = ''
    for x in str(text_seq):
        mapped_text = mapped_text + mapping[x]

    return mapped_text


# Fuction 5 for A3
def make_dict_from_lists(key_list, value_list):
    """Given:
        a key_list [k1, k2, k3, k4, ...] and
        a value_list [v1, v2, v3, v4, ...],
    Returns the dictionary with the mapping {k1:v1, k2:v2, k3:v3, k4:v4, ...}

    Precondition: both input lists are the same length. Also, the key_list
      contains no duplicate elements.
    """
    new_dict = {}
    for x in range(len(key_list)):
        item = {key_list[x]: value_list[x]}
        new_dict.update(item)
    return new_dict

# Fuction 6 for A3
def get_letter_counts(text):
    """
    Returns a dictionary with the following properties:
        * the keys are all the 26 letters of the alphabet plus " " (space)
        * the values are how many times the letters occured in the text
    text: (str) containing only letters a-z and spaces
    Example: "ab abc acb d" --> {'a':3, 'b':3, 'c':2, 'd':1, 'e':0, ... ' ':3}
    """
    counts = initialize_counts()
    for x in text:
        count = text.count(x)
        item = {x : count}
        counts.update(item)
    return counts # STUDENTS: you will want to use your initialize_counts fn!

# Fuction 7 for A3
def get_pair_counts(text):
    """
    Returns: a dictionary :
        * the keys are all two-letter combinations (pairs)
        * the values are how many times these pairs occured in the text
    text: (str) containing only letters a-z and spaces
    Example: "ab abc acb d" --> {'ab': 2, 'ac': 1, 'bc': 1, 'cb': 1, 'b ': 1, 'c ': 1, ' a': 2}
    """
    doubles = {}
    frq = 1
    for x in range(len(text)):
        if frq != len(text):
            count = text.count(text[x] + text[frq])
            item = {text[x] + text[x +1] : count}
            doubles.update(item)
            frq = frq + 1
    return doubles # STUDENTS: do NOT use your initialize_counts fn here

# -----------------------------------------------------------
#      STUDENTS: Do not change any of the code below!
# -----------------------------------------------------------

def sort_by_frequency(frequency_dict):
    """Given a dictionary whose values are integers, Returns a new dictionary
    whose key,value pairs are sorted in increasing order by value.

    Example: if given this dictionary: {'a':4, 'x':2, 'y':9, 'h':6}
         would return this dictionary: {'x':2, 'a':4, 'h':6, 'y':9}
    """
    # STUDENTS: this is some pretty ugly Python. Please don't spend
    # time trying to decipher it. :(
    if frequency_dict==None:
        return # avoids an Error when the code is not all there yet.
    tmplist = sorted((value, key) for (key,value) in frequency_dict.items())
    return dict([(k,v) for v,k in tmplist])

class FreqText():
    """
    Given a string, an instance is
    - the original string
    - information about letter frequencies of the text
    - information about letter pair frequencies of the text

    Example:
    """

    def __init__(self, text):
        """
        Document this!
        """
        self.txt = text
        letter_count_tmp = get_letter_counts(self.txt)
        self.letter_counts = sort_by_frequency(letter_count_tmp)
        self.pair_counts = get_pair_counts(self.txt)

def get_random_letter():
    """
    Returns a random letter from the alpha_list (@ top of this file)
    """
    # first get a random number from 0 to the length of the alphabet
    random_i = np.random.randint(0, len(alpha_list))
    # now use that random number to index into the alphabet list
    # and get a random letter
    random_letter = alpha_list[random_i]
    return random_letter

def clean_text(txt):
    """Returns a copy of txt but with all white space, numbers, and
    non-alpha characters replaced by spaces.
    Also replaces multiple spaces with single spaces.
    """
    txt = txt.replace('\n',' ')
    txt = txt.replace('\r',' ')
    txt = txt.lower();
    txt = re.sub(r'[^\w\s]', ' ', txt) # remove all punctuation
    txt = remove_numerics(txt)         # remove all numbers 0-9
    txt = remove_multiple_spaces(txt)  # replace multiple spaces w/1 space
    return txt

def text_to_file(text, filename):
    """Opens a file with the name `filename`, writes the string `text`
    to that file. Closes the file.
    """
    output_file = open(filename, "w")
    output_file.write(text)
    output_file.close()

def filename_to_clean_string(filename):
    """Opens a file with the name `filename`, reads the contents of the file
    into a string, closes the file, returns a "cleaned" version of the string.
    Closes the file.
    """
    file = open(filename)
    txt = clean_text(file.read())
    file.close()
    return txt

def generate_random_mapping():
    """Returns a random mapping of letters in the alpha_list to letters
    in the alpha_list.
    """
    mixed_alpha = np.random.permutation(alpha_list) # makes shuffled copy
    return make_dict_from_lists(alpha_list, mixed_alpha)

def generate_frequency_mapping(scrambled_counts, ref_counts):
    """ Takes 2 dictionaries and returns a new dictionary.

    ref_counts: keys are a-z & space. values are how often these characters
                appeared in the reference text.
    scrambled_counts: keys are a-z & space. values are how often these
                      characters appeared in the scrambled text.

    The keys of the dictionary are sorted from small to large values.
    Returns a new dictionary which maps the scrambled letters to the reference
    letters in order to match frequencies.
    Example: if in the reference text the least common letter is 'q'
             and in the scrambled text, the least common letter is 'e'
             our new `frequency mapping` should map 'e' to 'q'
             Similarly, if in the refernece text, the most common letter is ' '
             and in the scrambled text, the most common letter is 'l'
             our new `frequency mapping` should map 'l' to ' '
    """
    if ref_counts==None:
        return # avoids an Error when the code is not all there yet.
    ref_sorted_letter_list = list(ref_counts.keys())
    sorted_letter_list = list(scrambled_counts.keys())

    return make_dict_from_lists(sorted_letter_list, ref_sorted_letter_list)
