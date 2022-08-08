from dataclasses import dataclass

@dataclass 
class OctoData:
    intensity: int
    flashedThisStep: bool

class lazyDict(dict):
    def __missing__ (self, key):
        self[key] = OctoData(intensity=0, flashedThisStep = False)
        return self[key]

grid = lazyDict()

with open("input.txt", "r", encoding="utf-8") as infile:
    data = infile.read().split('\n')

numRows = len(data)
numCols = len(data[0])

#Load data into dict
for r in range(numRows):
    for c in range (numCols):
        grid[(r, c)] = OctoData(intensity = int(data[r][c]), flashedThisStep = False)

def printGrid(printFlashes = False ):
    for r in range(numRows):
        for c in range(numCols):
            val = grid[(r,c)].intensity
            if val <= 9: print(val, end = "")
            else: print("-", end = "")
        print("")

stepNumber = 0

printGrid()
print("--")

while True:
    stepNumber += 1
    #Increment by 1
    for r in range(numRows):
        for c in range(numCols):
            grid[(r,c)].intensity += 1

    while True:
        anyFlashesThisRound = False
        
        #Flash as necesasry
        for r in range(numRows):
            for c in range(numCols):
                if grid[(r,c)].intensity > 9 and grid[(r,c)].flashedThisStep == False:
                    grid[(r,c)].flashedThisStep = True
                    anyFlashesThisRound = True

                    for deltar in [-1,0,1]:
                        for deltac in [-1,0,1]:
                            if not(deltar == 0 and deltac == 0): grid[(r + deltar, c + deltac)].intensity += 1

        fts = [grid[(r,c)].flashedThisStep for r in range(numRows) for c in range(numCols)]

        if not anyFlashesThisRound: break

    for r in range(numRows):
        for c in range(numCols):
            if grid[(r,c)].flashedThisStep: grid[(r,c)].intensity = 0
            grid[(r,c)].flashedThisStep = False

    if sum([grid[(r,c)].intensity for r in range(numRows) for c in range(numCols)]) == 0: break


print("--")
print("final:")
printGrid()
print(f"All flashed on step {stepNumber}")