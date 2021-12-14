from dataclasses import dataclass

with open("input.txt", "r", encoding="utf-8") as infile:
    data = [line.split('-') for line in infile.read().split('\n')]

@dataclass
class Route():
    pathSoFar: list
    currentCave: str
    smallCavesVisited: dict #['a', numberOfTimesVisited]. This is the key change

startingPaths = [path for path in data if 'start' in path] 
routesInProgress = list()

for p in startingPaths:
    route = p.copy()
    s = p.copy()
    s.remove('start')
    current = s[0]
    if s[0] == s[0].lower(): smalls = {'start':0, str(s[0]):1}
    else: smalls = {'start':0}
    routesInProgress.append(Route(pathSoFar=','.join(route), smallCavesVisited = smalls, currentCave = current))

completeRoutes = list()

while(len(routesInProgress) > 0):
    nextRoutes = list()

    for r in routesInProgress:
        if r.currentCave == 'end':
            completeRoutes.append(r)
        else:
            nextPaths = [path for path in data if r.currentCave in path and 'start' not in path]
            for p in nextPaths:
                nextCave = [item for item in p if item != r.currentCave][0]

                if nextCave not in r.smallCavesVisited or (r.smallCavesVisited[nextCave] == 1 and not any([(v >= 2) for v in r.smallCavesVisited.values()])):
                    newPath = r.pathSoFar +',' + nextCave 
                    newSmallCaves = r.smallCavesVisited.copy()
                    if nextCave == nextCave.lower():
                        if nextCave in r.smallCavesVisited:
                            newSmallCaves[nextCave] += 1
                        else:
                            newSmallCaves[nextCave] = 1
                    nextRoutes.append(Route(pathSoFar = newPath, smallCavesVisited = newSmallCaves, currentCave = nextCave))

    routesInProgress = nextRoutes

print(f"Total routes: {len(completeRoutes)}")