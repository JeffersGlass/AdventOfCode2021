from dataclasses import dataclass

with open("input.txt", "r", encoding="utf-8") as infile:
    data = [line.split('-') for line in infile.read().split('\n')]

@dataclass
class Route():
    pathSoFar: list
    currentRoom: str
    littleRoomsVisited: dict #['a', numberOfTimesVisited]. This is the key change

startingPaths = [path for path in data if 'start' in path] 
routesInProgress = list()

for p in startingPaths:
    route = p.copy()
    s = p.copy()
    s.remove('start')
    current = s[0]
    if s[0] == s[0].lower(): littles = {'start':0, str(s[0]):1}
    else: littles = {'start':0}
    routesInProgress.append(Route(pathSoFar=','.join(route), littleRoomsVisited = littles, currentRoom = current))

#TODO Treat 'start' differently, adjust little-rooms-visited init
completeRoutes = list()

while(len(routesInProgress) > 0):
    nextRoutes = list()
    #print("")
    #print(f"ProcessingRoutes: {len(routesInProgress)}")
    #print(f"CompletedRoutes:  {len(completeRoutes)}")

    for r in routesInProgress:
        #print(f"Examining route {r}", end = "")
        #Check if we're reached the end
        if r.currentRoom == 'end':
            #print(", which is complete!")
            completeRoutes.append(r)
        else:
            #print("")
            nextPaths = [path for path in data if r.currentRoom in path and 'start' not in path]
            for p in nextPaths:
                #print(f"\tPossible next path: {p}", end = "")
                nextRoom = [item for item in p if item != r.currentRoom][0]
                #print(f" leading to room {nextRoom}", end ="")

                if nextRoom not in r.littleRoomsVisited or (r.littleRoomsVisited[nextRoom] == 1 and not any([(v >= 2) for v in r.littleRoomsVisited.values()])):
                    newPath = r.pathSoFar +',' + nextRoom #[p]
                    newLittleRooms = r.littleRoomsVisited.copy()
                    #print(" which is valid")
                    if nextRoom == nextRoom.lower():
                        if nextRoom in r.littleRoomsVisited:
                            newLittleRooms[nextRoom] += 1
                        else:
                            newLittleRooms[nextRoom] = 1
                    nextRoutes.append(Route(pathSoFar = newPath, littleRoomsVisited = newLittleRooms, currentRoom = nextRoom))
                else:
                    pass
                    #print(" but this is invalid")

    routesInProgress = nextRoutes
    #input("Press enter")

#for r in completeRoutes:
    #print(r)
print(f"Total routes: {len(completeRoutes)}")