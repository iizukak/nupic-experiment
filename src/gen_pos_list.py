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

DATA_DIR = "data/"

text = nltk.word_tokenize(webtext.raw("firefox.txt"))
pos_list = nltk.pos_tag(text)

with open(DATA_DIR + 'firefox.csv', 'w') as f:
    writer = csv.writer(f, encoding='utf-8')
    writer.writerows(pos_list)
