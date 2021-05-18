from numpy.lib.function_base import append
from functions import *
import pandas as pd
import numpy as np
import math

test_data = pd.read_csv('Test.csv')
train_data = pd.read_csv('Train.csv')

def printAnim(i, j):
    bar = [
    "[        ]",
    "[=       ]",
    "[===     ]",
    "[====    ]",
    "[=====   ]",
    "[======  ]",
    "[======= ]",
    "[========]",
    "[ =======]",
    "[  ======]",
    "[   =====]",
    "[    ====]",
    "[     ===]",
    "[      ==]",
    "[       =]",
    "[        ]",
    "[        ]"
    ]
    print(" {} Creating data {}/{} ".format(bar[i%len(bar)], i, j), end = "\r")

def finalizeData(list, id, fam_size, i, j):
    mode = list["Segmentation"].mode()
    list = list.query("Segmentation in @mode").sort_values("Family_Size")
    index = 0
    segmentation = list["Segmentation"].iloc[index]
    data.append([id, segmentation])
    printAnim(i, j)

def startAnalysis():
    rows = length(test_data)
    for i in range (0, rows):
        final_data = train_data
        person = {
            'ID':test_data["ID"][i],
            'Gender':test_data["Gender"][i],
            'Ever_Married':test_data["Ever_Married"][i],
            'Age':test_data["Age"][i],
            'Graduated':test_data["Graduated"][i],
            'Profession':test_data["Profession"][i],
            'Work_Experience':test_data["Work_Experience"][i],
            'Spending_Score':test_data["Spending_Score"][i],
            'Family_Size':test_data["Family_Size"][i],
            'Var_1':test_data["Var_1"][i],
        }
        fns = [
            {"metric":"Age", "Age": person["Age"], "min":person["Age"] - 3, "max":person["Age"] + 3},
            {"metric":"Work_Experience", "Work_Experience": person["Work_Experience"], "min":person["Work_Experience"] - 3, "max":person["Work_Experience"] + 3},
            {"metric":"Family_Size", "Family_Size": person["Family_Size"], "min":person["Family_Size"] - 3, "max":person["Family_Size"] + 3}
        ]
        for x in ["Gender", "Ever_Married", "Graduated", "Profession", "Spending_Score", "Var_1"]:
            if(length(final_data) > 0):
                tmp_final = final_data.query('{} == "{}"'.format(x, person[x]))
                if(length(tmp_final) > 0):
                    final_data = tmp_final
                else:
                    continue;

        for x in fns:
            if(length(final_data) > 0):
                max = (0) if math.isnan(x["max"]) else x["max"]
                min = (0) if math.isnan(x["min"]) else x["max"]
                tmp_data = final_data.query("{} <= {} & {} >= {}".format(x["metric"], max, x["metric"], min))
                if(length(tmp_final) > 0):
                    final_data = tmp_final
                else:
                    continue;
        finalizeData(final_data, person["ID"], person['Family_Size'], i, rows)
    
data = []
startAnalysis()
submission = pd.DataFrame(data, columns = ['ID', 'Segmentation'])
print(submission)
submission.to_csv('submission.csv', index=False)