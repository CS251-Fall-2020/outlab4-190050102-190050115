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

tests = [round(float(i), 3) for i in np.array(data[1][1:])]
infected = [round(float(i), 3) for i in np.array(data[2][1:])]
recovered = [round(float(i), 3) for i in np.array(data[3][1:])]
deceased = [round(float(i), 3) for i in np.array(data[4][1:])]

out = []
out.append(["Field", "Mean", "Std. Dev."])
out.append(["Tests", f'{np.mean(tests):.3f}', f'{np.std(tests):.3f}'])
out.append(["Infected", f'{np.mean(infected):.3f}', f'{np.std(infected):.3f}'])
out.append(["Recovered", f'{np.mean(recovered):.3f}', f'{np.std(recovered):.3f}'])
out.append(["Deceased", f'{np.mean(deceased):.3f}', f'{np.std(deceased):.3f}'])

widths = [max(map(len, col)) for col in zip(*out)]

for row in out:
    print("   ".join(val.ljust(width) for val, width in zip(row, widths)))


