#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script detect English Grammer Error
#

import nltk
import pprint
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.data.inference_shifter import InferenceShifter


model = ModelFactory.loadFromCheckpoint("model/")
model.disableLearning()
shifter = InferenceShifter()


def posErrDetect(target_str):
    # model.resetSequenceStates() 
    pos_list = nltk.pos_tag(nltk.word_tokenize(target_str))
    for row in pos_list:
        model_input = {"token": row[1]}
        result = shifter.shift(model.run(model_input))
        pprint.pprint(row)
        dic = result.inferences["multiStepPredictions"][1]
        if type(dic) == type({}):
            if dic.has_key(row[1]):
                print(dic[row[1]])
            else:
                print(0)
