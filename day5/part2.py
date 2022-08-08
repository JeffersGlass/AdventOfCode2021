import re
from collections import namedtuple

with open ("input.txt", 'r') as infile:
    data = infile.read().split("\n")

Line = namedtuple('Line', ['p1x', 'p1y', 'p2x', 'p2y'])
parsedData = []
for d in data:
    reg = re.search(r'(.+),(.+) -> (.+),(.+)', d)
    parsedData.append(Line(p1x = int(reg.group(1)), p1y = int(reg.group(2)), p2x = int(reg.group(3)), p2y = int(reg.group(4))))

horizontalLines = [l for l in parsedData if l.p1y == l.p2y]
verticalLines = [l for l in parsedData if l.p1x == l.p2x]

coveredOnce, coveredMany = set(), set()

for l in horizontalLines:
    for xCoord in range(min(l.p1x, l.p2x), max(l.p1x, l.p2x)+1):
        point = (xCoord, l.p1y)
        #If the point is already covered by multiple lines, we don't need to do anything more with it, but
        if point not in coveredMany:
            #If we haven't see it at all, we should mark that we've now seen it once.
            if point not in coveredOnce: 
                coveredOnce.add(point)
            #Otherwise, we should mark that we've now seen it in multiple lines
            else:
                coveredOnce.remove(point)
                coveredMany.add(point)

for l in verticalLines:
    for yCoord in range(min(l.p1y, l.p2y), max(l.p1y, l.p2y)+1):
        point = (l.p1x, yCoord)
        #If the point is already covered by multiple lines, we don't need to do anything more with it, but
        if point not in coveredMany:
            #If we haven't see it at all, we should mark that we've now seen it once.
            if point not in coveredOnce: 
                coveredOnce.add(point)
            #Otherwise, we should mark that we've now seen it in multiple lines
            else:
                coveredOnce.remove(point)
                coveredMany.add(point)

diagonalLines = [l for l in parsedData if l not in verticalLines and l not in horizontalLines]

for l in diagonalLines:
    #Make sure the first coordinate of each line is left of the second coordinte
    if l.p2x < l.p1x: l = Line(p1x = l.p2x, p1y = l.p2y, p2x = l.p1x, p2y = l.p1y)
    #Determine if y increases or descreases with increasing X
    yDir = 1 if l.p2y > l.p1y else -1

    for yDelta, xCoord in enumerate(range(l.p1x, l.p2x+1)):
        point = (xCoord, l.p1y + (yDelta*yDir))

        if point not in coveredMany:
            #If we haven't see it at all, we should mark that we've now seen it once.
            if point not in coveredOnce: 
                coveredOnce.add(point)
            #Otherwise, we should mark that we've now seen it in multiple lines
            else:
                coveredOnce.remove(point)
                coveredMany.add(point)

print(f"Solution is: {len(coveredMany)}")