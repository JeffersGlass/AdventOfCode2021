import re

with open("input.txt", "r", encoding="utf-8") as infile:
    data = infile.read().split('\n\n')

points = set([(int(line.split(",")[0]), int(line.split(",")[1])) for line in data[0].split('\n')])

foldPattern = r'fold along (.)=(\d+)'
folds = [(re.search(foldPattern, line).group(1),int(re.search(foldPattern, line).group(2))) for line in data[1].split('\n')]

def executeFold(points, f):
    if f[0] == 'x': return doXFold(points, f)
    elif f[0] == 'y': return doYFold(points, f)
    else: raise ValueError(f"Expected fold in x or y, got fold {f}")

def doXFold(points, f):
    return set([p if p[0] < f[1] else (f[1] - (p[0] - f[1]), p[1]) for p in points])

def doYFold(points, f):
    retSet = set()
    for p in points:
        if p[1] < f[1]: retSet.add(p)
        else: retSet.add((p[0], f[1] - (p[1] - f[1])))
    return retSet

def printPoints(points):
    maxX = max([p[0] for p in points])
    maxY = max([p[1] for p in points])
    for y in range(maxY+1):
        for x in range(maxX+1):
            if (x, y) in points: print("X", end = "")
            else: print(".", end = "")
        print("")

if __name__ == "__main__":
    for f in folds:
        points = executeFold(points, f)
    printPoints(points)