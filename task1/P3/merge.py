import csv
import numpy as np

file_lock = "mumbai_data.csv"

with open(file_lock,'r') as f:
    reader = csv.reader(f)     

    for i, row in enumerate(reader):
        if i == 0: 
            lock = [[] for _ in range(len(row))]

        for j, col in enumerate(row):
            lock[j].append(col)


file_unlock = "mumbai_unlock.csv"

with open(file_unlock,'r') as f:
    reader = csv.reader(f)     

    for i, row in enumerate(reader):
        if i == 0: 
            unlock = [[] for _ in range(len(row))]

        for j, col in enumerate(row):
            unlock[j].append(col)

day = lock[0]

test_rate = ["Positivity Rate(Lock)"]
test_rate += [ f'{float(key)/float(lock[1][i+1]):.3f}' for i, key in enumerate(lock[2][1:])]

tests = ["Infected(lock)"]
tests += [ i for i in lock[1][1:]]

test_rate2 = ["Positivity Rate(Unlock)"]
test_rate2 += [ f'{float(key)/float(unlock[1][i+1]):.3f}' for i, key in enumerate(unlock[2][1:])]

tests2 = ["Infected(Unlock)"]
tests2 += [ i for i in unlock[1][1:]]

out = [day, tests, tests2, test_rate, test_rate2]

out = np.transpose(out)
out2 = [ i.tolist() for i in out]

with open("info_combine.csv", 'w', newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(out2)
