from collections import defaultdict

data = defaultdict(lambda:100)

with open("input.txt", "r", encoding="utf-8") as infile:
    raw = infile.read().split('\n')
    numRows = len(raw)
    numCols = len(raw[0])
    for r, row in enumerate(raw):
        for c, col in enumerate(row):
            data[(r, c)] = int(col)

total = 0

for r in range(numRows):
    for c in range(numCols):
        #print([(r + deltar, c + deltac) for deltar in [-1, 0, 1] for deltac in [-1, 0, 1] if (deltar*deltac == 0 and deltar != deltac)])
        if all([data[(r, c)] < data[(r + deltar, c + deltac)] for deltar in [-1, 0, 1] for deltac in [-1, 0, 1] if (deltar*deltac == 0 and deltar != deltac)]):
            total += data[(r, c)] + 1


print(f"{total= }")