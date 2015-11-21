#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unicodecsv as csv
from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.modelfactory import ModelFactory
import pprint

import model_params.model_params as model_params
import pos_tags

DATA_DIR = "data/"
INPUT_FILE = "firefox-pos-list.csv"

def addCategoryEncoder(params):
    params["modelParams"]["sensorParams"]["encoders"].update({ 
        "token": {
            "fieldname": u"token",
            "name": u"token",
            "type": "CategoryEncoder",
            "categoryList": pos_tags.TAG_IDS,
            "w": 23
        }
    })
    # pprint.pprint(params)
    return params

def getModel():
    model = ModelFactory.create(addCategoryEncoder(model_params.MODEL_PARAMS))
    model.enableInference({"predictedField": "token"})
    return model

def createModelAndRun():
    model = getModel()
    

# getModel()
shifter = InferenceShifter()

