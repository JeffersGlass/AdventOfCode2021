from dataclasses import dataclass
from typing import Any
from termcolor import colored, cprint

with open("input_test.txt", "r", encoding="utf-8") as infile:
    data = infile.read().split('\n')

risk = dict()
for y, line in enumerate(data):
    for x, val in enumerate(line):
        risk[(x, y)] = int(val)

maxY = len(data)
maxX = len(data[0])

@dataclass
class PointData():
    g_cost: int
    parent: Any

def h_cost(point):
    return 14 * min(point[0], point[1]) + 10 * abs(point[1]-point[0])

def getNeighbors(point):
    nList = list()
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if (0 <= point[0] + x < maxX) and (0 <= point[1] + y < maxY): nList.append((point[0] + x, point[1] + y))
    
    return nList

def cost(location: tuple, point: PointData):
    return point.g_cost + h_cost(location)

def printMap(openPoints, closedPoints, activePoint):
    for y in range(maxY):
        for x in range(maxX):
            val = risk[(x,y)]
            if (x,y) == activePoint: cprint(val, 'grey', 'on_green', end="")
            elif (x,y) in closedPoints: cprint(val, 'red', end="")
            elif (x,y) in openPoints: cprint(val, 'green', end="")
            else:cprint(val, 'white', end="")
        print("")

def findPath(start, end):
    openPoints = {start: PointData(g_cost=0, parent=None)}
    closedPoints = dict()

    while True:
        input("")
        costList = sorted([p for p in openPoints], key= lambda p:cost(p, openPoints[p]))
        if len(costList) > 0: lowestCostPoint = costList[0]
        else: break #???

        printMap(openPoints, closedPoints, lowestCostPoint)
        print(f"Cheapest next point is {lowestCostPoint}:{openPoints[lowestCostPoint]}")
        #input("Press enter")
        if lowestCostPoint == end: break 


        closedPoints[lowestCostPoint] = openPoints[lowestCostPoint]
        del openPoints[lowestCostPoint]

        for newPoint in getNeighbors(lowestCostPoint):
            if newPoint not in closedPoints:
                print(f"Exploring neighbor {newPoint} of {lowestCostPoint}")
                if newPoint not in openPoints or (risk[newPoint] + cost(lowestCostPoint, closedPoints[lowestCostPoint])) < 100000000: #TODO or new path to neighbor is cheaper
                    newFCost = closedPoints[lowestCostPoint].g_cost + risk[newPoint]
                    newData = PointData(g_cost=newFCost, parent = lowestCostPoint)
                    openPoints[newPoint] = newData #should always happen?

            else:
                pass

    print("DONE!")
    while True:
        p = 1

if __name__ == '__main__':
    findPath((0,0), (10,10))