import numpy as np
import pandas as pd

filename = "mumbai_data.csv"

fields = [] 
rows = [] 

cols = ["Tests", "Infected", "Recovered", "Deceased"]
data = pd.read_csv(filename, usecols=cols)

tests = np.array(data.Tests.tolist())
infected = np.array(data.Infected.tolist())
recovered = np.array(data.Recovered.tolist())
deceased = np.array(data.Deceased.tolist())


out = []
out.append(["Field", "Mean", "Std. Dev."])
out.append(["Tests", str(np.mean(tests).round(decimals=2)), str(np.std(tests).round(decimals=2))])
out.append(["Infected", str(np.mean(infected).round(decimals=2)), str(np.std(infected).round(decimals=2))])
out.append(["Recovered", str(np.mean(recovered).round(decimals=2)), str(np.std(recovered).round(decimals=2))])
out.append(["Deceased", str(np.mean(deceased).round(decimals=2)), str(np.std(deceased).round(decimals=2))])

# print(out)

widths = [max(map(len, col)) for col in zip(*out)]

for row in out:
    print("   ".join(val.ljust(width) for val, width in zip(row, widths)))


