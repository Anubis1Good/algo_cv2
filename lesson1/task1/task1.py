import numpy as np

regions = []
deltas = []
inflation = 1.07

with open('./task1/regions.txt') as file:
    lines = file.readlines()
    for line in lines:
        regions.append(line.split())
with open('./task1/delta.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        deltas.append(line.split(', '))


regions = np.array(regions,dtype=np.float64)
deltas = np.array(deltas,dtype=np.float64)
total = regions + deltas
total *= inflation

print(total)