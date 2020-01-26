import os
import json
import pickle

# This file preprocesses the dictionary.json that we have in our repo
# The output is a pickled list of words from the dictionary

dir_path = os.path.dirname(os.path.realpath(__file__))
dictionary_path = os.path.join(dir_path, 'data', 'dictionary.json')

# # We use the json module to obtain a python dictionary
# from the json file
with open(dictionary_path) as fd:
    dictionary_dict = json.load(fd)

# We're not interested in the word definitions so
# we can throw that away.
word_list = list(dictionary_dict.keys())
print('Length of generatred list: {}'.format(len(word_list)))

# Finally, we pickle the list of words we'd like to
# check as available usernames on instagram later on
pickle_path = os.path.join(dir_path, 'data', 'word_list.pickle')
with open(pickle_path, 'wb') as f:
    pickle.dump(word_list, f)