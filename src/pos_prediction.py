#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script is main module of this repository.
# Predict next word's POS in the sentence.
#

import nltk
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.data.inference_shifter import InferenceShifter


model = ModelFactory.loadFromCheckpoint("model/")
model.disableLearning()
shifter = InferenceShifter()


def predictPOS(target_str):
    pos_list = nltk.pos_tag(nltk.word_tokenize(target_str))
    ret = []
    for row in pos_list:
        model_input = {"token": row[1]}
        result = shifter.shift(model.run(model_input))
        dic = result.inferences["multiStepPredictions"][1]
        if type(dic) == type({}):
            if dic.has_key(row[1]):
                ret.append((row[0], row[1], dic[row[1]]))
            else:
                ret.append((row[0], row[1], 0.0))
        else:
            ret.append((row[0], row[1], 0.0))
    return ret
