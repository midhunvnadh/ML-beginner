#! /bin/python3
from numpy.lib.function_base import append
from functions import *
import pandas as pd
import numpy as np

test_data = pd.read_csv('Test.csv')
train_data = pd.read_csv('Train.csv')

def finalizeData(list, id, i, j):
    mode = list["Segmentation"].mode()
    list = list.query("Segmentation in @mode").sort_values("Family_Size")
    segmentation = list["Segmentation"].iloc[0]
    data.append([id, segmentation])
    printAnim(i, j, "Creating Data")

def startAnalysis():
    cls()
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
        alg_order = [
            {'met':"Gender", 'num':False},
            {'met':"Ever_Married", 'num':False},
            {'met':"Graduated", 'num':False},
            {'met':"Profession", 'num':False},
            {'met':"Spending_Score", 'num':False},
            {'met':"Var_1", 'num':False},
            {'met':"Age", 'num':True, 'gi':10},
            {'met':"Family_Size", 'num':True, 'gi':5},
            {'met':"Work_Experience", 'num':True, 'gi':1}
        ]
        for x in alg_order:
            if(x["num"]):
                if(length(final_data) > 0):
                    tmp_final = final_data.iloc[(final_data[x["met"]]-person[x["met"]]).abs().argsort()[:int(x['gi'])]]
                    if(length(tmp_final) > 0):
                        final_data = tmp_final
                    else:
                        continue
            else:
                if(length(final_data) > 0):
                    tmp_final = final_data.query('{} == "{}"'.format(x["met"], person[x["met"]]))
                    if(length(tmp_final) > 0):
                        final_data = tmp_final
                    else:
                        continue
        finalizeData(final_data, person["ID"], i, rows)
    
data = []
startAnalysis()
print ("\033[A                                        \033[A")
submission = pd.DataFrame(data, columns = ['ID', 'Segmentation'])
print(submission)

filename = 'submission.csv'
submission.to_csv(filename, index=False)

check_accuracy(filename)