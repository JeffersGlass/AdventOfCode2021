with open("input.txt", "r") as infile:
    data = [int(t) for t in infile.read().split('\n')]

triples = zip(data[:-2], data[1:-1], data[2:])
windowSums = [sum(list(t)) for t in triples]

numDecreases = len([t for t in zip(windowSums[:-1], windowSums[1:]) if t[0] < t[1]])

print(f"{numDecreases=}")
