from dataclasses import dataclass

with open("input.txt", "r", encoding="utf-8") as infile:
    data = [line.split('-') for line in infile.read().split('\n')]

@dataclass
class Route():
    pathSoFar: list
    currentRoom: str
    littleRoomsVisited: list

startingPaths = [path for path in data if 'start' in path]
routesInProgress = [Route(pathSoFar=[s], littleRoomsVisited= ['start'] if not(all([item == item.lower() for item in s])) else s, currentRoom = list(set(s) - {'start'})[0]) for s in startingPaths]
completeRoutes = list()

while(len(routesInProgress) > 0):
    nextRoutes = list()
    print("")
    print(f"ProcessingRoutes: {len(routesInProgress)}")
    print(f"CompletedRoutes:  {len(completeRoutes)}")

    for r in routesInProgress:
        #Check if we're reached the end
        if r.currentRoom == 'end':
            completeRoutes.append(r)
            print(f"Route completed {r}")
        else:
            print(f"Examining route {r}")
            nextPaths = [path for path in data if r.currentRoom in path]
            for p in nextPaths:
                print(f"\tPossible next path: {p}", end = "")
                nextRoom = [item for item in p if item != r.currentRoom][0]
                print(f", next room would be {nextRoom}", end = "")
                if nextRoom not in r.littleRoomsVisited:
                    newPath = r.pathSoFar + [p]
                    if nextRoom == nextRoom.lower():
                        newLittleRooms = r.littleRoomsVisited + [nextRoom]
                    else:
                        newLittleRooms = r.littleRoomsVisited
                    nextRoutes.append(Route(pathSoFar = newPath, littleRoomsVisited = newLittleRooms, currentRoom = nextRoom))
                    print(", so we'll check that next time")
                else:
                    print(", but already been to that little room")

    routesInProgress = nextRoutes
    #input("Press enter")

print("_______")
print("COMPLETE ROUTES")
for r in completeRoutes:
    print(r)
print(len(completeRoutes))