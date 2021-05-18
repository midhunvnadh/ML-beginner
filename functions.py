import pandas as pd


def printAnim(i, j, message):
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
    print(" {} {} {}/{} ".format(bar[i%len(bar)], message, i, j), end = "\r")

def length(list):
    return list.shape[0]

def check_accuracy(filename, filename2):
    print("\n")
    data1 = pd.read_csv(filename)
    data2 = pd.read_csv(filename2)
    rows = length(data2)
    counter = 1
    for x in range (0, rows):
        submission = data1.iloc[x]
        submission_ref = data2.query("ID == {}".format(submission["ID"])).get(key = 'Segmentation').values[0]

        submission_sec = submission.get(key = 'Segmentation')
        if(submission_sec == submission_ref):
            counter = counter + 1
        printAnim(counter, rows, "Analyzing Score")
    print ("\033[A                             \033[A")
    print("Score: {}".format(counter/rows))