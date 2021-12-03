with open("input.txt", 'r') as infile:
    inputdata = infile.read().split('\n')

def mostCommonDigitInPosition(data, position):
    return "1" if sum([int(num[position]) for num in data]) >= len(data)/2 else "0"

#find Oxygen Rating
oxyData = [d for d in inputdata]
co2Data = [d for d in inputdata]

for i in range(len(inputdata[0])):
    if len(oxyData) <= 1: break
    MCD_o2 = mostCommonDigitInPosition(oxyData, i)
    oxyData = [t for t in oxyData if t[i] == MCD_o2]

for i in range(len(inputdata[0])):
    if len(co2Data) <= 1: break
    MCD_co2 = mostCommonDigitInPosition(co2Data, i)
    co2Data = [t for t in co2Data if t[i] != MCD_co2]

if len(oxyData) == 1: oxygenRating = int(oxyData[0], 2)
else: raise ValueError(f"Oxygen Data should only have one element, instead was {oxyData}")

if len(co2Data) == 1: co2Rating = int(co2Data[0], 2)
else: raise ValueError(f"CO2 Data should only have one element, instead was {co2Data}")

print(f"Product: {oxygenRating * co2Rating= }")