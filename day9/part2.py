from collections import defaultdict
from math import prod

data = defaultdict(lambda:9)

with open("input.txt", "r", encoding="utf-8") as infile:
    for r, row in enumerate(infile.read().split('\n')):
        numRows = r + 1
        for c, col in enumerate(row):
            numCols = c + 1
            data[(r, c)] = int(col)

total = 0
basins = list()

for r in range(numRows):
    for c in range(numCols):
        if all([data[(r, c)] < data[(r + deltar, c + deltac)] for deltar in [-1, 0, 1] for deltac in [-1, 0, 1] if (deltar*deltac == 0 and deltar != deltac)]):
            basins.append([(r, c),])

basinLengths = []
for b in basins:
    for pos in b:
        b.extend([(pos[0] + deltar, pos[1] + deltac) for deltar in [-1, 0, 1] for deltac in [-1, 0, 1] \
            if (deltar*deltac == 0 and deltar != deltac and \
                data[(pos[0] + deltar, pos[1] + deltac)] != 9 and \
                    (pos[0] + deltar, pos[1] + deltac) not in b)])
    basinLengths.append(len(b))

print(f"Solution: {prod(sorted(basinLengths, reverse=True)[:3])}")