import pandas as pd
import os
from get_score import get_score

def cls():
    if os.name == 'posix':
        _ = os.system('reset')
    else:
        _ = os.system('cls')

def printAnim(i, j, message):
    bar = [
        "[          ]",
        "[*         ]",
        "[**        ]",
        "[***       ]",
        "[****      ]",
        "[*****     ]",
        "[******    ]",
        "[*******   ]",
        "[********  ]",
        "[********* ]",
        "[ *********]",
        "[  ********]",
        "[   *******]",
        "[    ******]",
        "[     *****]",
        "[      ****]",
        "[       ***]",
        "[        **]",
        "[         *]",
        "[          ]"
    ]
    print(" {} {} {}/{} ".format(bar[i%len(bar)], message, i, j), end = "\r")

def length(list):
    return list.shape[0]

def check_accuracy(filename):
    print ("\nScore = ", get_score(filename))