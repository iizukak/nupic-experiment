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
from nltk.corpus import brown

DATA_DIR = "data/"

pos_list = brown.tagged_words(categories='news')
output_path = DATA_DIR + "news-pos-list.csv"
print(output_path, "Writing to CSV")
with open(output_path, 'w') as f:
    writer = csv.writer(f, encoding='utf-8')
    writer.writerows(pos_list)

print(output_path + " closed")
