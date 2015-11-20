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

for fileid in webtext.fileids():
    print("Tokenizing Text for" + fileid)
    text = nltk.word_tokenize(webtext.raw(fileid))
    print("Analysing POS tag...")
    pos_list = nltk.pos_tag(text)

    output_path = DATA_DIR + fileid.replace(".txt", "") + "-pos-list.csv"
    print(output_path, "Writing to CSV")
    with open(output_path, 'w') as f:
        writer = csv.writer(f, encoding='utf-8')
        writer.writerows(pos_list)

    print(output_path + " closed")
