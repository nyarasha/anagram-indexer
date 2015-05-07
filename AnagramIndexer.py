"""
AnagramIndexer.py:
Given a word input by the user, prints out the rank of that word within the alphabetical list of all possible anagrams
"""

import collections
import math

__author__ = 'Karen Wickert'

def get_word_from_user():
    """
    get input word from the user, validates input
    :return: word formatted to lowercase containing only letter characters
    """
    user_word = raw_input("Please enter a word: ")
    print "You entered:", user_word

    # check that input string contains only letters
    while not user_word.isalpha():
        print "Oops! That wasn't a valid word. Please enter a word containing only alphabetical characters."
        user_word = raw_input("Please enter a word: ")
        print "You entered:", user_word

    # convert word to lowercase
    lowercase_word = user_word.lower()

    return lowercase_word


def get_number_of_letter_permutations(permute_word):
    """
    Finds the number of permutations of letters in a given word
    :param permute_word: a word to find permutations of
    :return: number of permutations of letters in the word
    """
    # find all letter combinations to get the numerator of the permutation expression
    letter_combinations = math.factorial(len(permute_word))

    # create letter frequency map to find total number of permutations
    letter_frequencies = collections.Counter(permute_word)

    # multiply all the frequency values of letters to get the denominator for permutations
    letter_freq_product = 1
    for letter_frequency in letter_frequencies.values():
        letter_freq_product *= math.factorial(letter_frequency)

    # combine the expressions above to calculate permutations
    letter_permutations = letter_combinations / letter_freq_product

    return letter_permutations


# Memory profiling
# import os
# def memory_usage_psutil():
#     # return the memory usage in MB
#     import psutil
#     process = psutil.Process(os.getpid())
#     mem = process.get_memory_info()[0] / float(2 ** 20)
#     return mem


rank = 1

word = get_word_from_user()

# Runtime tracking
#import time
#start_time = time.time()

# arrange letters in alphabetical order to keep track of letters available
# this is the anagram of the letters of the user word which has rank 1, the optimal arrangement
sorted_available_letters = ''.join(sorted(word))

# check the user word against the sorted available letters to test against all possible anagrams
# in descending alphabetical order
word_index = 0
available_index = 0
# begin with the first letter of the word
current_letter = word[word_index]
while sorted_available_letters != '':
    # if the letters of the sorted word and the user word match
    if current_letter == sorted_available_letters[available_index]:
        # remove this letter from the available letters
        if len(sorted_available_letters) > 1:
            sorted_available_letters = "{0}{1}".format(sorted_available_letters[:available_index],
                                                       sorted_available_letters[available_index + 1:])
            word_index += 1
            current_letter = word[word_index]
            available_index = 0
        else:
            # finished looking through all the letters available - exit loop
            sorted_available_letters = ''

    # if the letters of the sorted word and the user word don't match
    else:
        # add number of permutations of anagrams that start with the alphabetical letters to the ranking
        # since all those anagrams come alphabetically before the word chosen by the user
        rank += get_number_of_letter_permutations(
            sorted_available_letters[:available_index] + sorted_available_letters[available_index + 1:])
        # move to the next unique letter in the sorted available letters
        current_sorted_letter = sorted_available_letters[available_index]
        while sorted_available_letters[available_index] == current_sorted_letter:
            available_index += 1

print "Alphabetical rank of your word in all possible anagrams:", rank

# Print out memory usage
# print "Memory usage (MB):", memory_usage_psutil()

# Print out run time
#print "%s seconds" % (time.time() - start_time)
