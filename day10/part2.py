from statistics import median

with open ("input.txt", "r", encoding='utf-8') as infile:
    data = infile.read().split("\n")

lefts  = [ '(',     '[',    '{',    '<' ]
rights = [ ')',     ']',    '}',    '>' ]
points = [ 1,       2,      3,      4   ]

scores = list()

def autocompleteScore(stack):
    score = 0
    for item in stack[::-1]:
        score = (score * 5) + points[lefts.index(item)]
    return score

for line in data:
    isCorrupt = False
    stack = list()
    for char in line:
        if char in lefts:
            stack.append(char)
        elif char in rights:
            lastLeft = stack.pop()
            if lefts.index(lastLeft) != rights.index(char):
                break
        else: raise ValueError(f"Unkown character {char}")
    else:
        scores.append(autocompleteScore(stack))

""" print(autocompleteScore([ \
    '<', \
    '{', \
    '(', \
    '[' \
])) """

print(f"{scores= }")
print(f"{median(scores)= }")