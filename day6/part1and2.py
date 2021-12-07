with open("input.txt", "r") as infile:
    inputdata = [int(num) for num in infile.read().split(',')]

fishcounts = [inputdata.count(num) for num in range(0,8+1)]
daysToRun = 256

for _ in range(daysToRun):
    newfishcounts = fishcounts[1:] + [fishcounts[0]]
    newfishcounts[6] += fishcounts[0]
    fishcounts = newfishcounts

print(f"After {daysToRun} days there are {sum(fishcounts)} lanternfish")