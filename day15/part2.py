from dataclasses import dataclass
from typing import Any
from maputils import mapDisplay
from astarutils import calc_h_cost
from time import time

showMaps = False

with open("input.txt", "r", encoding="utf-8") as infile:
    data = infile.read().split('\n')

originalRisk = dict()
for y, line in enumerate(data):
    for x, val in enumerate(line):
        originalRisk[(x, y)] = int(val)

original_maxY = len(data)
original_maxX = len(data[0])

risk = dict()
for x_copy in range(5):
    for y_copy in range(5):
        for i in range(original_maxX):
            for j in range(original_maxY):
                risk[(x_copy*original_maxX + i, y_copy*original_maxY + j)] = (originalRisk[(i,j)] + x_copy + y_copy - 1) % 9 + 1

maxY = original_maxY * 5
maxX = original_maxX * 5
totalPoints = maxY * maxY

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

def findPath(start, end):
    locationScores = {start: PointData(f_cost = 0, parent=None)}
    openPoints = {start}
    closedPoints = set()

    oldSelection = [0,0]
    stepPrint = 1000
    steps = 0

    startTime = time()

    while True:
        if showMaps:
            m = mapDisplay(maxX, maxY, risk, locationScores=locationScores, openPoints=openPoints, closedPoints=closedPoints, oldSelection = oldSelection)
            if m.retCode['exitcode'] == 1: exit()
            else: oldSelection = m.retCode['selection']

        costList = sorted([p for p in openPoints], key= lambda p:locationScores[p].f_cost)
        if len(costList) > 0: lowestCostPoint = costList[0]
        else: break #???

        #printMap(openPoints, closedPoints, lowestCostPoint)
        #print(f"Cheapest next point is {lowestCostPoint}:{locationScores[lowestCostPoint]}")
        if lowestCostPoint == end: break 

        closedPoints.add(lowestCostPoint)
        openPoints.remove(lowestCostPoint)
        if (steps := steps+1) % stepPrint == 0: print(f"After {steps} step: {len(closedPoints)= } {len(openPoints)= } of {totalPoints} after {round(time() - startTime, 2)}")

        for newPoint in getNeighbors(lowestCostPoint):
            if newPoint not in closedPoints:
                #print(f"Exploring neighbor {newPoint} of {lowestCostPoint}")
                if newPoint not in openPoints: #  or (risk[newPoint] + cost(lowestCostPoint, closedPoints[lowestCostPoint])) < 100000000: #TODO or new path to neighbor is cheaper
                    newFCost = locationScores[lowestCostPoint].f_cost + calc_h_cost(newPoint, end) + risk[newPoint]
                    locationScores[newPoint] = PointData(f_cost=newFCost, parent = lowestCostPoint)
                    if newPoint not in openPoints:
                        openPoints.add(newPoint)
            else:
                pass

    scoringPoint = lowestCostPoint
    totalRisk = 0
    pathPoints = [scoringPoint]
    #print("Calculating Path Score:")
    while locationScores[scoringPoint].parent != None:
        if showMaps:
            m = mapDisplay(maxX, maxY, risk, locationScores=locationScores, openPoints=openPoints, closedPoints=closedPoints, pathPoints=pathPoints, oldSelection = oldSelection, pathLength=totalRisk)
            if m.retCode['exitcode'] == 1: exit()
            else: oldSelection = m.retCode['selection']

        totalRisk += risk[scoringPoint]
        scoringPoint = locationScores[scoringPoint].parent
        pathPoints.append(scoringPoint)

    #totalRisk -= risk[(0,0)]

    print(f"{totalRisk= }")

if __name__ == '__main__':
    findPath((0,0), (maxX-1, maxY-1))