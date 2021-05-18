#! /bin/python3
from numpy.lib.function_base import append
from functions import *
import pandas as pd
import numpy as np

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

def finalizeData(list, id, i, j):
    mode = list["Segmentation"].mode()
    list = list.query("Segmentation in @mode").sort_values("Family_Size")
    segmentation = list["Segmentation"].iloc[0]
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
        for x in ["Gender", "Ever_Married", "Graduated", "Profession", "Spending_Score", "Var_1"]:
            if(length(final_data) > 0):
                tmp_final = final_data.query('{} == "{}"'.format(x, person[x]))
                if(length(tmp_final) > 0):
                    final_data = tmp_final
                else:
                    continue
        gi = 3
        for x in ["Age", "Family_Size", "Work_Experience"]:
            if(length(final_data) > 0):
                tmp_final = final_data.iloc[(final_data[x]-person[x]).abs().argsort()[:gi]]
                if(length(tmp_final) > 0):
                    final_data = tmp_final
                else:
                    continue
            gi = gi - 1
        finalizeData(final_data, person["ID"], i, rows)
    
data = []
startAnalysis()
submission = pd.DataFrame(data, columns = ['ID', 'Segmentation'])
print(submission)
submission.to_csv('submission.csv', index=False)