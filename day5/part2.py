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
diagonalLines = [l for l in parsedData if l not in verticalLines and l not in horizontalLines]

coveredOnce, coveredMany = set(), set()

#Loop over all the points in the lines we care about
for l in horizontalLines:
    #print(f"Processing horizontal line from ({l.p1x},{l.p1y}) to ({l.p2x},{l.p2y})")
    #print(f"\tProcessing Points")
    for xCoord in range(min(l.p1x, l.p2x), max(l.p1x, l.p2x)+1):
        point = (xCoord, l.p1y)
        #print(f"\t\t{point} ", end = "")
        #If the point is already covered by multiple lines, we don't need to do anything more with it, but
        if point not in coveredMany:
            #If we haven't see it at all, we should mark that we've now seen it once.
            if point not in coveredOnce: 
                coveredOnce.add(point)
                #print(" has now been seen once")
            #Otherwise, we should mark that we've now seen it in multiple lines
            else:
                coveredOnce.remove(point)
                coveredMany.add(point)
                #print(" was seen once before, has now been seen multiple times")
        else:
            pass
            #print("Has already been seen multiple times")
    #print(f"\t{len(coveredMany)} points are covered at least twice")

#Loop over all the points in the lines we care about
for l in verticalLines:
    #print(f"Processing vertical line from ({l.p1x},{l.p1y}) to ({l.p2x},{l.p2y})")
    #print(f"\tProcessing Points")
    for yCoord in range(min(l.p1y, l.p2y), max(l.p1y, l.p2y)+1):
        point = (l.p1x, yCoord)
        #print(f"\t\t{point} ", end = "")
        #If the point is already covered by multiple lines, we don't need to do anything more with it, but
        if point not in coveredMany:
            #If we haven't see it at all, we should mark that we've now seen it once.
            if point not in coveredOnce: 
                coveredOnce.add(point)
                #print(" has now been seen once")
            #Otherwise, we should mark that we've now seen it in multiple lines
            else:
                coveredOnce.remove(point)
                coveredMany.add(point)
                #print(" was seen once before, has now been seen multiple times")
        else:
            pass
            #print("Has already been seen multiple times")
    #print(f"\t{len(coveredMany)} points are covered at least twice")

#loop over all the diagonal lines:
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
                #print(" has now been seen once")
            #Otherwise, we should mark that we've now seen it in multiple lines
            else:
                coveredOnce.remove(point)
                coveredMany.add(point)
                #print(" was seen once before, has now been seen multiple times")
        else:
            pass
            #print("Has already been seen multiple times")

print(f"Solution is: {len(coveredMany)}")