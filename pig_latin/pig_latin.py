import string
""" Problem 3: Pig Latin.

   Author:      Jinghua Xu
   Description: a simple transformation of English text into Pig Latin
   Honor Code:  I pledge that this program represents my own work.
"""


def encode_word(word):
    """Method for encoding an English word in Pig Latin.

    Parameters
    ----------
    word : string
        The word to encode.

    Returns
    -------
    encoded_word:
        The word encoded in Pig Latin.
    """

    # argument check: empty string argument
    if word == '':
        return word

    encoded_word = word
    puncts_at_end = ""
    # set of puncts
    puncts = string.punctuation
    # set of vowels
    set_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # getting rid of the puctuation(s) at the end of the word(iteration starts from the end of the word): detect and store ending puncts
    for char in word[::-1]:
        if char not in puncts:
            break
        else:
            # store puncts in reverse order
            puncts_at_end += char
            # remove detected punct at the end from encoded word, puncts will be added back to encoded_word at last
            encoded_word = encoded_word[:-1]
        # reverse the puncts since it was stored in reversed order, this will later be added to the end of encoded_word, which currently is free of puncts at the end
        puncts_at_end = puncts_at_end[::-1]

    # detect and move consonants cluster at the beginning of the input word
    for _ in range(len(encoded_word)):
        if encoded_word[0] in set_vowels:
            break
        else:
            # move the consonant to the ned of the word
            encoded_word = encoded_word[1:] + encoded_word[0]

    # brief and logical version: case1: all upper case situation, case2: not all uppercase(capitalization? handled in this case)
    if word.isupper():
        encoded_word += 'AY'
    else:
        encoded_word += 'ay'
        # taking care of capitalization
        if word.istitle():
            encoded_word = encoded_word.title()
        # this lower operation won't be needed if strictly follows the functionality description in readme file, but to pass the tests based on test data, lower() is required to fit with the expected output in the test
        else:
            encoded_word = encoded_word.lower()

    # add ending puncts
    encoded_word = encoded_word + puncts_at_end
    return encoded_word


def encode_file_1(input_file, output_file):
    """Method for converting a file containing English text to Pig Latin.
    Concatenates each newly converted word to a string containing the already converted text, then writes the fullly converted text to file.

    Parameters
    ----------
    input_file : Path
        The pathlib.Path to the input file containing English text.
    output_file : Path
        The pathlib:Path to the output file containing the Pig Latin text.

    Returns:
        None

    Results by test_speed():
    Timing  20  loops of encode_file_1:  7.265606766
    """
    output_str = ''
    with open(input_file, 'r', encoding='utf8') as reader:
        for line in reader.readlines():
            # handling empty lines
            if line.isspace():
                output_str += '\n' + line
            else:
                words = line.split()
                for word in words:
                    output_str += encode_word(word) + ' '

    with open(output_file, 'w', encoding='utf8') as writer:
        writer.write(output_str)


def encode_file_2(input_file, output_file):
    """Method for converting a file containing English text to Pig Latin.
    Appends each newly converted word to a list containing the already converted words, then writes the fullly converted text to file using ''.join([word_list]).

    Parameters
    ----------
    input_file : Path
        The pathlib.Path to the input file containing English text.
    output_file : Path
        The pathlib:Path to the output file containing the Pig Latin text.

    Returns:
        None
    Results by test_speed():
    Timing  20  loops of encode_file_2:  7.505761064999999 
    """
    str_list = list()
    with open(input_file, 'r', encoding='utf8') as reader:
        for line in reader.readlines():
            # handling empty lines
            if line.isspace():
                str_list.append('\n' + line)
            else:
                words = line.split()
                for word in words:
                    str_list.append(encode_word(word) + ' ')

    output_str = ''.join(str_list)

    with open(output_file, 'w', encoding='utf8') as writer:
        writer.write(output_str)
