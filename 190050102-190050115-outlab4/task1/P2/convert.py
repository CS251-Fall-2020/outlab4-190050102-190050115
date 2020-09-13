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

test_rate = ["Test Positivity rate"]
test_rate += [ float(key)/float(data[1][i+1]) for i, key in enumerate(data[2][1:])]
test_rate[1:] = np.round_(test_rate[1:], decimals=3)


tests = ["Tests per Million"]
tests += [ int(i)/20.4 for i in data[1][1:]]
tests[1:] = np.round_(tests[1:])
tests[1:] = [int(i) for i in tests[1:]]

recovered = ["Recovered"]
recovered += [i for i in data[3][1:]]

Deceased = ["Deceased"]
Deceased += [i for i in data[4][1:]]

days = data[0]

out = [days, tests, test_rate, recovered, Deceased]

out = np.transpose(out)
out2 = [ i.tolist() for i in out]


with open("transformed.csv", 'w', newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(out2)