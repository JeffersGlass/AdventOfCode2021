from dataclasses import dataclass

with open("input.txt", "r", encoding="utf-8") as infile:
    data = [line.split('-') for line in infile.read().split('\n')]

@dataclass
class Route():
    pathSoFar: list
    currentRoom: str
    littleRoomsVisited: list # of tuples: ['a', numberOfTimesVisited]

startingPaths = [path for path in data if 'start' in path]

#TODO Treat 'start' differently, adjust little-rooms-visited init
routesInProgress = [Route(pathSoFar=[s], littleRoomsVisited= ['start'] if not(all([item == item.lower() for item in s])) else s, currentRoom = list(set(s) - {'start'})[0]) for s in startingPaths]
completeRoutes = list()

while(len(routesInProgress) > 0):
    nextRoutes = list()

    for r in routesInProgress:
        #Check if we're reached the end
        if r.currentRoom == 'end':
            completeRoutes.append(r)
        else:
            nextPaths = [path for path in data if r.currentRoom in path]
            for p in nextPaths:
                nextRoom = [item for item in p if item != r.currentRoom][0]
                #TODO Treat littleRoomsViisted differently based on new rules for p2
                if nextRoom not in r.littleRoomsVisited:
                    newPath = r.pathSoFar + [p]
                    if nextRoom == nextRoom.lower():
                        #TODO Treat littleRoomsViisted differently based on new rules for p2
                        newLittleRooms = r.littleRoomsVisited + [nextRoom]
                    else:
                        newLittleRooms = r.littleRoomsVisited
                    #TODO Treat littleRoomsViisted differently based on new rules for p2
                    nextRoutes.append(Route(pathSoFar = newPath, littleRoomsVisited = newLittleRooms, currentRoom = nextRoom))
                else:
                    pass

    routesInProgress = nextRoutes
    #input("Press enter")

print(f"Total routes: {len(completeRoutes)}")