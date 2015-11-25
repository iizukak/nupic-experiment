#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unicodecsv as csv
from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.modelfactory import ModelFactory
import pprint
import os

import model_params.model_params as model_params
import pos_tags

DATA_DIR = "data/"
INPUT_FILE = "news-pos-list.csv"
MODEL_DIR = os.getcwd() + "/model"

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
    return params


def createModel(verbosity=False):
    model = ModelFactory.create(addCategoryEncoder(model_params.MODEL_PARAMS))
    model.enableInference({"predictedField": "token"})

    if verbosity:
        print(model)

    return model


def main():
    model = createModel(verbosity = True)
    shifter = InferenceShifter()

    input_file_name = DATA_DIR + INPUT_FILE
    output_file_name = DATA_DIR + "out.csv"

    countor = 1
    with open(input_file_name, 'r') as f1, open(output_file_name, 'w') as f2:
        reader = csv.reader(f1)
        writer = csv.writer(f2)
        for row in reader:
            model_input = {"token": row[1]}
            result = shifter.shift(model.run(model_input))

            if countor % 100 == 0:
                print("input line:", countor)
            if countor % 1000 == 0:
                print("result:", result)
            if countor % 5000 == 0:
                print("save model")
                model.save(MODEL_DIR)

            writer.writerow(row + [result.inferences["anomalyScore"]])

            countor += 1
    print("saving model to", MODEL_DIR)
    model.save(MODEL_DIR)

if __name__ == "__main__":
    main()

