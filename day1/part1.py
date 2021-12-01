with open("input.txt", "r") as infile:
    data = [int(t) for t in infile.read().split('\n')]

pairs = zip(data[:-1], data[1:])

numDecreases = len([pair for pair in zip(data[:-1], data[1:]) if pair[0] < pair[1]])

print(f"{numDecreases=}")
