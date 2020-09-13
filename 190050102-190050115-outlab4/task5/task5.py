import csv
import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats

csv_url = "https://api.covid19india.org/csv/latest/case_time_series.csv"

df = pd.read_csv(csv_url)
k = df[df['Date'] == '14 April '].index.values
df.drop(df.index[:k[0]],inplace = True)

deaths = df['Total Deceased'].tolist()
n = len(deaths)

y = []

for i in range(1,n):
	y.append(float(deaths[i])/float(deaths[i-1]))


x = list(range(1,n))

slope, intercept, r_value, p_value, std_err= stats.linregress(x,y)
yline = [slope*xx + intercept for xx in x]
plt.scatter(x, y, s=40, facecolors='none', edgecolors='b',label ='Data')
plt.plot(x,yline,'r',label ='Regression line')
plt.xlabel("t(days after 15 April)")
plt.ylabel("H(t) = x(t)/x(t-1)")
plt.title("H(t) vs t (Levitt's metric)")
plt.legend()
plt.savefig("covid.png")
plt.close()

day = int(np.ceil((1-intercept)/slope))
print(day)


