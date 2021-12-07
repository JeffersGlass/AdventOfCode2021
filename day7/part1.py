from statistics import median

with open("input.txt", "r") as infile:
    data = [int(num) for num in infile.read().split(',')]

median = median(data)
minFuel = sum([abs(d-median) for d in data])

print(f"{minFuel= }")