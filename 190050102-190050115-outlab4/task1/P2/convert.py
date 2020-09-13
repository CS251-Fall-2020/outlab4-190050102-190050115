import csv
import numpy as np

filename = "mumbai_data.csv"

with open('mumbai_data.csv','r') as f:
    reader = csv.reader(f)     

    for i, row in enumerate(reader):
        if i == 0: 
            data = [[] for _ in range(len(row))]

        for j, col in enumerate(row):
            data[j].append(col)

cols = ["Tests", "Infected", "Recovered", "Deceased"]

out = []

test_rate = ["Test Positive Rate"]
test_rate += [ f'{float(key)/float(data[1][i+1]):.3f}' for i, key in enumerate(data[2][1:])]

tests = ["Tests per Million"]
tests += [ int(int(i)/20.4) for i in data[1][1:]]

recovered = ["Recovered"]
recovered += [f'{float(i):.3f}' for i in data[3][1:]]

Deceased = ["Deceased"]
Deceased += [f'{float(i):.3f}' for i in data[4][1:]]

days = data[0]

out = [days, tests, test_rate, recovered, Deceased]

out = np.transpose(out)
out2 = [ i.tolist() for i in out]


with open("transformed.csv", 'w', newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(out2)