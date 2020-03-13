import os
import pandas as pd

import xmltodict
import json
tctr_trials = []

for file in os.listdir():
    if file.endswith('.xml'):
        with open(os.path.join(file), encoding = "ISO-8859-1") as xml:
            doc = xmltodict.parse(xml.read())
            trials_trials=[]
            for trial in doc['trials']['trial']:
                 tctr_trials.append(json.dumps(trial))


from datetime import date
import csv

def tctr_csv():
    with open('tctr1.csv','w', newline = '') as tctr_csv:
        writer=csv.writer(tctr_csv)
        for val in tctr_trials:
            writer.writerow([val])

tctr_csv()



