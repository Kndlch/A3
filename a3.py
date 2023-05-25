# a3.py
# Prof. Bracy, AWB93
# Feb 10, 2023

import numpy as np
import a3_helper

"""See CS1110 Spring '23 A3 writeup."""

# -------------------------------------------------------------------
#      STUDENTS: This is not a file you will submit. You are welcome
# to play around (change the print frequency or the number of tries,
# or even the name of the file you want to decrypt), but nothing you
# do here will be seen or graded by us. So make sure your changes are
# not needed in order to run your code in a3_helper.py
# -------------------------------------------------------------------

# how many times we'll change the mapping to try to get a better decoding
NUM_TRIES = 3001
PRINT_FREQUENCY = 400

def score(mapping, text, ref_ftext):
    """Scores the mapping by asking: If I use `mapping` to decrypt
    `text`, how similar will the resulting letter pair frequencies be to
    the letter pair frequencies of my reference text, `ref_ftext`?

    mapping: the decryption we want to score. Mapping is a dictionary that
       maps characters to characters. For example, the entry 'a':'x' means
       that every occurence of 'a' in `text` should be replaced with 'x'.
    text: the (scrambled) string we are trying to decrypt
    ref_ftext: the reference text we're using (e.g., War and Peace).
        an obejct of type FreqText which means we've already calculated
        the letter pair frequencies for the text (how convenient!)

    Returns a float based on math that is beyond the scope of CS 1110
    """
    # First, decode `text` using `mapping`
    decoded_text = a3_helper.apply_mapping(text, mapping)
    # Next, create a FreqText object from the decoded text. This object
    # has an attribute `pair_counts` that is the frequencies of the letter
    # pairs given this mapping.
    curr_ftext = a3_helper.FreqText(decoded_text)

    # Finally, for each letter pair combination in the `text` (decoded
    # with `mapping`) how often does that pair occur in the reference text?
    key_score = 0
    if curr_ftext.pair_counts == None:
        return -100 # avoids Error when code unfinished
    for k,v in curr_ftext.pair_counts.items():
        if k in ref_ftext.pair_counts:
            key_score += v*np.log(ref_ftext.pair_counts[k])
    return key_score

def get_new_mapping(mapping):
    """ Takes a decryption mapping, randomly selects two letters, and swaps the
    values for those letter keys. So if `mapping` maps 'a' to 'x' and 'b' to 'q'
    then the new mapping maps 'a' to 'q' and 'b' to 'x'.
    Returns this new mapping, a dictionary.
    """
    if mapping==None:
        return # avoid an Error when the code is not all there yet
    new_mapping = mapping.copy() # does not change the input dictionary
    # randomly select two letters to swap
    # yes, they might happen to be the _same_ letter, but it's okay
    # since we will do this so many times....
    k1 = a3_helper.get_random_letter()
    k2 = a3_helper.get_random_letter()

    # Okay we did this for you and we don't expect you to do this on your
    # own, but check out this line below. It swaps 2 dictionary entries.
    # Behold the awesomeness that is Python:
    new_mapping[k1],new_mapping[k2] = new_mapping[k2],new_mapping[k1]
    return new_mapping

### MAIN PROGRAM

if __name__ == '__main__':

    # here is the encoded/scrambled file
    encoded_text = a3_helper.filename_to_clean_string('secret_scramble.txt')
    print('\nScrambled text:')
    print(encoded_text)

    # the reference text from which we learn about English letter frequencies
    reference_text = a3_helper.filename_to_clean_string("warandpeace.txt")

    # Get statistics about the reference and scrambled texts
    ref_ftext = a3_helper.FreqText(reference_text)
    encoded_ftext = a3_helper.FreqText(encoded_text)

    # begin with an intelligent initial mapping
    curr_mapping = a3_helper.generate_frequency_mapping(
        encoded_ftext.letter_counts, ref_ftext.letter_counts)
    curr_score = score(curr_mapping, encoded_text, ref_ftext)

    # now let's repeatedly try to find a better mapping.
    print('\nROUND:         CURRENT DECRYPTION OF SCRAMBLED TEXT     ')
    print('--------------------------------------------------------')
    for i in range(NUM_TRIES):
        # randomly swap 2 letters in the scrambled text. is it better?
        new_decrypt_mapping = get_new_mapping(curr_mapping)
        new_score = score(new_decrypt_mapping, encoded_text, ref_ftext)

        # if new is better than curr, is_better is positive
        is_better = (new_score - curr_score)/min(10000/(i+1),1)

        # generate a random number between 0 and 1
        runif = np.log(np.random.uniform())

        # use random number to weight whether we accept the new mapping
        # or not. This improves our results for reasons beyond CS 1110.
        if runif < is_better:
            curr_mapping = new_decrypt_mapping
            curr_score = new_score

        # every now and then, show the progress we are making
        if (i%PRINT_FREQUENCY == 0):
            curr_text = a3_helper.apply_mapping(encoded_text, curr_mapping)
            print(format(i, '04d'), ":",curr_text[0:79],"\n\t",
                  curr_text[79:159])

    print('\nDecrypted text:')
    print(a3_helper.apply_mapping(encoded_text, curr_mapping))

    print("Decryption score: "+str(int(curr_score)))
