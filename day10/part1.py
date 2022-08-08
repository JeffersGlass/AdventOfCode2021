with open ("input.txt", "r", encoding='utf-8') as infile:
    data = infile.read().split("\n")

lefts  = [ '(',     '[',    '{',    '<' ]
rights = [ ')',     ']',    '}',    '>' ]
points = [ 3,       57,     1197,   25137]

totalScore = 0

for line in data:
    stack = list()
    for char in line:
        if char in lefts:
            stack.append(char)
        elif char in rights:
            lastLeft = stack.pop()
            if lefts.index(lastLeft) != rights.index(char):
                totalScore += points[rights.index(char)]
                break
        else: raise ValueError(f"Unkown character {char}")
    else:
        continue

print(f"{totalScore= }")