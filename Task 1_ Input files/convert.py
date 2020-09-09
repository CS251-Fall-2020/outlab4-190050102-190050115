import csv
import numpy as np

data = []

with open("mumbai_data.csv") as f:
    reader = csv.reader(f)
    for row in csv.reader(f, delimiter=','):
        data.append(row)

# print(data)
d = np.array(data[1:])

for i in d:
    print(i[1:])
    for j in i[1:]:
        j = float(j)
    print(np.mean(i[1:]))