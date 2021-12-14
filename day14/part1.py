import re
from collections import Counter

with open("input.txt", "r", encoding="utf-8") as infile:
    data = infile.read().split("\n\n")

template = data[0]
rules = dict()
for line in data[1].split('\n'):
    r = re.search(r'(..) -> (.)', line)
    rules[r.group(1)] = r.group(2)

def doStep(template):
    additions = [" "] * len(template)
    for i in range(len(template[:-1])):
        letterPair = template[i:i+2]
        if letterPair in rules: additions[i] = rules[letterPair]
    
    return ''.join([val for pair in zip(template, additions) for val in pair] + [template[-1]])

for i in range(10):
    template = doStep(template)

counts = Counter(template)
lCount = sorted(counts.items(), key=lambda x: x[1])

minimum, maximum = lCount[0][1], lCount[-1][1]
print(f"Result is {maximum - minimum= }")