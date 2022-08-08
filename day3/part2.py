with open("input.txt", 'r') as infile:
    inputdata = infile.read().split('\n')

def mostCommonDigitInPosition(data, position):
    return "1" if sum([int(num[position]) for num in data]) >= len(data)/2 else "0"

def leastCommonDigitInPosition(data, position):
    return "0" if sum([int(num[position]) for num in data]) >= len(data)/2 else "1"

def calculateRating(data, digitFunc):
    for i in range(len(data[0])):
        if len(data) <= 1: break
        digitToMatch = digitFunc(data, i)
        data = [t for t in data if t[i] == digitToMatch]

    if len(data) == 1: return int(data[0], 2)
    else: raise ValueError(f"Function calculateRating should termiante with one element, instead was {data}")

oxygenRating = calculateRating(inputdata, mostCommonDigitInPosition)
co2Rating = calculateRating(inputdata, leastCommonDigitInPosition)

print(f"Product: {oxygenRating} * {co2Rating} {oxygenRating * co2Rating= }")