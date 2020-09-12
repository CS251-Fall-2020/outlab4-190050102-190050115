import pandas as pd
import matplotlib.pyplot as plt
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--data", required=True, help="Data file")

data_file = ap.parse_args().data

data = pd.read_csv("sml.csv")
data = data.groupby(['instance'], as_index=False)
datas = [data.get_group(x) for x in data.groups]




inst1 = datas[0].groupby(['algorithm', 'epsilon'], as_index=False)
inst1 = [inst1.get_group(x) for x in inst1.groups]

fig, ax = plt.subplots()

for sub_inst in inst1:
    algo = sub_inst.algorithm.mode().values[0]
    if(algo == 'epsilon-greedy'):
        epsilon = sub_inst.epsilon.mode().values[0]
        algo = algo+" with epsilon="+str(epsilon)

    sub_inst = sub_inst.groupby(['horizon']).sample(n=50)
    sub_inst = sub_inst.groupby(['horizon']).mean()

    ax = sub_inst.plot(kind='line', y='REG', logx=True, logy=True, ax=ax, label=algo)

plt.ylabel('Regret')
plt.title('Instance 1 - both axes in log scale')

plt.savefig('instance1.png')




inst2 = datas[0].groupby(['algorithm', 'epsilon'], as_index=False)
inst2 = [inst2.get_group(x) for x in inst2.groups]

fig, ax = plt.subplots()

for sub_inst in inst2:
    algo = sub_inst.algorithm.mode().values[0]
    if(algo == 'epsilon-greedy'):
        epsilon = sub_inst.epsilon.mode().values[0]
        algo = algo+" with epsilon="+str(epsilon)

    sub_inst = sub_inst.groupby(['horizon'], as_index=False).sample(n=50)
    sub_inst = sub_inst.groupby(['horizon'], as_index=False).mean()
    ax = sub_inst.plot(kind='line', y='REG', logx=True, logy=True, ax=ax, label=algo)

plt.ylabel('Regret')
plt.title('Instance 2 - both axes in log scale')
plt.savefig('instance2.png')




inst3 = datas[0].groupby(['algorithm', 'epsilon'], as_index=False)
inst3 = [inst3.get_group(x) for x in inst3.groups]

fig, ax = plt.subplots()

for sub_inst in inst3:
    algo = sub_inst.algorithm.mode().values[0]
    if(algo == 'epsilon-greedy'):
        epsilon = sub_inst.epsilon.mode().values[0]
        algo = algo+" with epsilon="+str(epsilon)

    sub_inst = sub_inst.groupby(['horizon'], as_index=False).sample(n=50)
    sub_inst = sub_inst.groupby(['horizon'], as_index=False).mean()

    ax = sub_inst.plot(kind='line', y='REG', logx=True, logy=True, ax=ax, label=algo)

plt.ylabel('Regret')
plt.title('Instance 3 - both axes in log scale')
plt.savefig('instance3.png')






