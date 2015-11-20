#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script generate POS sequence CSV
#
#
# References
#
# NLTK: Accessing Text Corpora and Lexical Resources
# http://www.nltk.org/book/ch02.html
#
# NLTK: Categorizing and Tagging Words
# http://www.nltk.org/book/ch05.html
#

import nltk
import unicodecsv as csv
from nltk.corpus import webtext

import pos_tag_id

DATA_DIR = "data/"

print("Tokenizing Text...")
text = nltk.word_tokenize(webtext.raw("firefox.txt"))
print("Analysing POS tag...")
pos_list = nltk.pos_tag(text)

# Add POS tag ID
# ("cat", "NN") -> ("cat", "NN", 20)
pos_list = map(lambda x: (x[0], x[1], pos_tag_id.TAG_IDS[x[1]]), pos_list)

print("Writing to CSV...")
with open(DATA_DIR + 'firefox-pos-list.csv', 'w') as f:
    writer = csv.writer(f, encoding='utf-8')
    writer.writerows(pos_list)
