# a3_scramble.py
# Prof. Bracy, AWB93
# Feb 10, 2023

"""See CS1110 Spring '23 A3 writeup."""

"""This script will take in a file to scramble, scramble it,
   and then print out the scrambled version to another file.
   It also prints the mapping it used to a file.

   You run the script by typing at the command line:
   > python a3_scramble.py <filename>.txt

   where <filename> is a text file that you want to scramble.
   Your file name must end in ".txt"

   The scrambled output of your text will be written to the file
   <filename>_scramble.txt

   The mapping used will be written to the file
   <filename>_mapping.txt

   EXAMPLE:
   > python a3_scramble.py test.txt
   scrambling file: test.txt
   writing mapping to file: test_mapping.txt
   writing scrambled text to file: test_scramble.txt
   >
"""

import sys, cornellasserts, a3_helper

def generate_output_filename(suffix):
    filename = sys.argv[1] # string with the format <filename>.txt
    return filename[:-4] + suffix + ".txt"

def get_filename_from_command_line():
    # make sure the user gave us the name of a file to scramble
    # when user types "python a3_scramble.py test.txt"
    # the argument list to python is length 2.
    cornellasserts.assert_equals(2, len(sys.argv), "\nError: From the command"+
    " line, please provide exactly one filename to scramble.\n")
    # We want the argument at index 1, the name of the input file
    filename = sys.argv[1]
    # is the filename at least as long as "x.txt" ?
    cornellasserts.assert_true(len(filename) >= 5, "\nError: Filename must be"+
    " of the format `<filename>.txt`. Your filename is too short!\n")
    # does the filename end in ".txt" ?
    cornellasserts.assert_equals(".txt", filename[-4:], "\nError: Filename"+
    " must be of the format `<filename>.txt`. Yours does not end in '.txt'\n")
    return filename

if __name__ == '__main__':

    # get the name of the file we want to scramble
    filename = get_filename_from_command_line()
    print("scrambling file: "+filename)

    # get a clean version of the text in the input file
    text_to_scramble = a3_helper.filename_to_clean_string(filename)

    # generate a random mapping to scramble the text
    mapping = a3_helper.generate_random_mapping()
    mapping_filename = generate_output_filename("_mapping")
    print("writing mapping to file: "+mapping_filename)
    a3_helper.text_to_file(repr(mapping), mapping_filename)

    # scramble the text
    scrambled_text = a3_helper.apply_mapping(text_to_scramble, mapping)

    # get the output file name, based on the input file name
    output_filename = generate_output_filename("_scramble")

    # print scrambled text to an output file named output_filename
    print("writing scrambled text to file: "+output_filename)
    a3_helper.text_to_file(scrambled_text, output_filename)
