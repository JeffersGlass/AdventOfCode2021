from statistics import median

with open("input.txt", "r") as infile:
    data = [int(num) for num in infile.read().split(',')]

def fuelUsed(crabPositions, position):
    return sum([(abs(d - position)*(abs(d-position)+1)/2) for d in crabPositions])

class lazyDict(dict):
    def __init__ (self, factory):
        self.factory = factory
    def __missing__ (self, key):
        self[key] = self.factory(key)
        return self[key]

fuelToReach = lazyDict(lambda x: fuelUsed(data, x))

med = median(data)
fuelToReach[med] = fuelUsed(data, med)
testVal = med

while not ((fuelToReach[testVal] < fuelToReach[testVal+1]) and (fuelToReach[testVal] < fuelToReach[testVal-1])):
    if fuelToReach[testVal-1] < fuelToReach[testVal]: testVal -= 1
    elif fuelToReach[testVal+1] < fuelToReach[testVal]: testVal += 1
    else: raise ValueError(f"Something has gone wrong\n {fuelToReach= }")

print(f"Minimum required fuel is reached at position {testVal} with {fuelToReach[testVal]} fuel used")
print(f"Calculated {len(fuelToReach)} potential positions")


