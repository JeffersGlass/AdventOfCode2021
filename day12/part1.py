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

    for r in routesInProgress:
        if r.currentRoom == 'end':
            completeRoutes.append(r)
        else:
            #Get all path segments including hte current room
            nextPaths = [path for path in data if r.currentRoom in path]
            for p in nextPaths:
                #Get the room this path segment would lead to (it's the room that's not our current room)
                nextRoom = [item for item in p if item != r.currentRoom][0]
                #Can't go to a little room twice
                if nextRoom not in r.littleRoomsVisited:
                    newPath = r.pathSoFar + [p]
                    if nextRoom == nextRoom.lower():
                        #If we're now going to be in a little room, add it to the list of little rooms we've visited
                        newLittleRooms = r.littleRoomsVisited + [nextRoom]
                    else:
                        #Otherwise, the list of little rooms visited doens't change
                        newLittleRooms = r.littleRoomsVisited
                    nextRoutes.append(Route(pathSoFar = newPath, littleRoomsVisited = newLittleRooms, currentRoom = nextRoom))
                else:
                    pass

    routesInProgress = nextRoutes

print(f"Total routes: {len(completeRoutes)}")