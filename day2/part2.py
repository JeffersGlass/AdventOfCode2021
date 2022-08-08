with open("input.txt", 'r') as infile:
    # data is a list of tuples; each tuple is of form ('instruction', int) where 'instruction' is forward, down, up
    data = [(line.split(' ')[0], int(line.split(' ')[1])) for line in infile.read().split('\n')]

horizontal, depth, aim = 0,0,0

for d in data:
    match d:
        case ('down', num):
            aim += num
        case ('up', num):
            aim -= num
        case ('forward', num):
            horizontal += num
            depth += aim * num
        case _:
            raise ValueError(f"Unmatched instruction {d}")

print(f"Solution is {horizontal*depth= }")