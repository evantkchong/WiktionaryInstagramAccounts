import os
import re
import pickle
from tqdm import tqdm
from utils import split_list

# This file preprocesses the text file containing all article titles on wiktionary
# The output is a pickled list of words from the dictionary

dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = 'enwiktionary-20191120-all-titles-in-ns0'
file_path = os.path.join(dir_path, os.pardir, 'tmp', file_name)

# We loop through the file once to obtain the line count so that
# tqdm can display progress telemetry
with open(file_path) as f:
    for i, lines in enumerate(f):
        pass
    num_lines = i + 1

pattern = re.compile(r'[^a-z_]')

with tqdm(total=num_lines) as pbar:
    with open(file_path) as fd:
        word_list = []
        for line in fd:
            word = line.strip().lower()
            if pattern.search(word) is None and 1 < len(word) <= 30:
                # We also remove underscores from the words as presumably,
                # good instagram usenames do not use underscores
                word_list.append(word.replace('_', ''))
            pbar.update(1)
print('Length of generatred list: {}'.format(len(word_list)))
print('{0:.3g}% of wiktionary words are usable'.format(len(word_list)*100/num_lines))

# Next, we split the list of words into several equally sized lists
# to make it easier to handle
list_of_list_of_words = split_list(word_list, 26)


# Finally, we pickle the lists of words we'd like to
# check as available usernames on instagram later on
pickle_dir = os.path.join(dir_path, os.pardir, 'data', 'preprocessed')
if not os.path.exists(pickle_dir):
    os.makedirs(pickle_dir)

for i, word_list in enumerate(list_of_list_of_words):
    pickle_path =  os.path.join(pickle_dir, 'word_list_{}.pickle'.format(i+1))
    with open(pickle_path, 'wb') as f:
        pickle.dump(word_list, f)
