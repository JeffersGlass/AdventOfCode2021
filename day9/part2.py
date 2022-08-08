from collections import defaultdict
from math import prod

data = defaultdict(lambda:9)

with open("input.txt", "r", encoding="utf-8") as infile:
    raw = infile.read().split('\n')
    numRows = len(raw)
    numCols = len(raw[0])
    for r, row in enumerate(raw):
        for c, col in enumerate(row):
            data[(r, c)] = int(col)

basins = list()

#Find the low point for each bsain (as in part 1)
for r in range(numRows):
    for c in range(numCols):
        if all([data[(r, c)] < data[(r + deltar, c + deltac)] for deltar in [-1, 0, 1] for deltac in [-1, 0, 1] if (deltar*deltac == 0 and deltar != deltac)]):
            basins.append([(r, c),])

#Flood fill each basin until it hits a wall 
basinLengths = []
for b in basins:
    for pos in b:
        b.extend([(pos[0] + deltar, pos[1] + deltac) for deltar in [-1, 0, 1] for deltac in [-1, 0, 1] if (deltar*deltac == 0 and deltar != deltac and data[(pos[0] + deltar, pos[1] + deltac)] != 9 and (pos[0] + deltar, pos[1] + deltac) not in b)])
    basinLengths.append(len(b))

print(f"Solution: {prod(sorted(basinLengths, reverse=True)[:3])}")