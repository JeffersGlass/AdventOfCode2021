import sys

with open("input.txt", "r") as infile:
    data = [int(t) for t in infile.read().split('\n')]

pairs = zip(data[:-1], data[1:])
for p in pairs:
    pass
    #print(f"{p} {'I' if p[0] < p[1] else '<< DEC'}")
numDecreases = len([pair for pair in zip(data[:-1], data[1:]) if pair[0] < pair[1]])
numIncreases = len([pair for pair in zip(data[:-1], data[1:]) if pair[0] > pair[1]]) 
numEquals = len([pair for pair in zip(data[:-1], data[1:]) if pair[0] == pair[1]]) 

print(f"{numDecreases=} {numIncreases=} {numEquals=}")
