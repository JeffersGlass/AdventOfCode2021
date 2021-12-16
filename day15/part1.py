from dataclasses import dataclass
from typing import Any
from termcolor import colored, cprint
from maputils import mapDisplay
from astarutils import calc_h_cost

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
    f_cost: int
    parent: Any

def getNeighbors(point):
    nList = list()
    for delta in [(-1,0),(0,1),(1,0),(0,-1)]:
        testPoint = (point[0]+delta[0], point[1] + delta[1])
        if (0 <= testPoint[0] < maxX) and (0 <= testPoint[1] < maxY): nList.append(testPoint)
    
    return nList

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
    locationScores = {start: PointData(f_cost = 0, parent=None)}
    openPoints = [start]
    closedPoints = list()

    oldSelection = [0,0]

    while True:
        m = mapDisplay(maxX, maxY, risk, locationScores=locationScores, openPoints=openPoints, closedPoints=closedPoints, oldSelection = oldSelection)
        if m.retCode['exitcode'] == 1: exit()
        else: oldSelection = m.retCode['selection']

        costList = sorted([p for p in openPoints], key= lambda p:locationScores[p].f_cost)
        if len(costList) > 0: lowestCostPoint = costList[0]
        else: break #???

        #printMap(openPoints, closedPoints, lowestCostPoint)
        #print(f"Cheapest next point is {lowestCostPoint}:{locationScores[lowestCostPoint]}")
        if lowestCostPoint == end: break 

        closedPoints.append(lowestCostPoint)
        openPoints.remove(lowestCostPoint)

        for newPoint in getNeighbors(lowestCostPoint):
            if newPoint not in closedPoints:
                #print(f"Exploring neighbor {newPoint} of {lowestCostPoint}")
                if newPoint not in openPoints: #  or (risk[newPoint] + cost(lowestCostPoint, closedPoints[lowestCostPoint])) < 100000000: #TODO or new path to neighbor is cheaper
                    newFCost = locationScores[lowestCostPoint].f_cost + calc_h_cost(newPoint, end) + risk[newPoint]
                    locationScores[newPoint] = PointData(f_cost=newFCost, parent = lowestCostPoint)
                    if newPoint not in openPoints:
                        openPoints.append(newPoint)
            else:
                pass

    scoringPoint = lowestCostPoint
    totalRisk = 0
    pathPoints = [scoringPoint]
    print("Calculating Path Score:")
    while locationScores[scoringPoint].parent != None:
        m = mapDisplay(maxX, maxY, risk, locationScores=locationScores, openPoints=openPoints, closedPoints=closedPoints, pathPoints=pathPoints, oldSelection = oldSelection, pathLength=totalRisk)
        if m.retCode['exitcode'] == 1: exit()
        else: oldSelection = m.retCode['selection']

        totalRisk += risk[scoringPoint]
        scoringPoint = locationScores[scoringPoint].parent
        pathPoints.append(scoringPoint)

    printMap(pathPoints, [], [])
    print(f"{totalRisk= }")

if __name__ == '__main__':
    findPath((0,0), (9,9))