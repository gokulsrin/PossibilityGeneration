import pandas as pd 
import numpy as np 
import json
import http.client

#read entire csv
df = pd.read_csv("fullSample_FirstVignettes.csv")
#create headings text
cheadings = ["S1-FR_" + str(i) for i in range(4, 9)]
#get relevent headings
data = df[cheadings]
#row 1
rows = data.iloc[[i for i in range(0, len(data))]].to_numpy()
print(rows)
#sentiment analysis
conn = http.client.HTTPSConnection("twinword-sentiment-analysis.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "738964bbbemsh589575de604beaep123452jsn73e2e1faafe8",
    'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com"
    }
arr = []
for i in range(0, len(data)):
    row = rows[i]
    #seperate words with '%20'
    textstem = "/analyze/?text="
    sentiments = {}
    for pos in row:
        req = ""
        words = pos.split(" ")
        for word in words:
            req += word + "%20"
        text = textstem + req
        conn.request("GET", text , headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        sentiments[pos] = data.get("score")
        arr.append(sentiments)
print(arr)

