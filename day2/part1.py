with open("input.txt", 'r') as infile:
    # data is a list of tuples; each tuple is of form ('instruction', int) where 'instruction' is forward, down, up
    data = [(line.split(' ')[0], int(line.split(' ')[1])) for line in infile.read().split('\n')]

horizontal = sum([step[1] for step in data if step[0] == 'forward'])
depth = sum([step[1] for step in data if step[0] == 'down']) - sum([step[1] for step in data if step[0] == 'up'])
print(f"Solution product is {horizontal * depth =}")