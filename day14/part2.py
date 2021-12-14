import re
from collections import Counter

with open("input.txt", "r", encoding="utf-8") as infile:
    data = infile.read().split("\n\n")

firstLetter = data[0][0]
lastLetter = data[0][-1]

template = dict()
for i in range(len(data[0])-1):
        letterPair = data[0][i:i+2]
        template[letterPair] = (template[letterPair] + 1 if letterPair in template else 1)

rules = dict()
for line in data[1].split('\n'):
    r = re.search(r'(..) -> (.)', line)
    rules[r.group(1)] = (r.group(1)[0] + r.group(2), r.group(2) + r.group(1)[1])


def doStep(template):
    print(f"Processing Template {template}")
    newTemplate = dict()
    for pairOfLetters in template:
        #print(f"Processing letter pair {pairOfLetters}")

        nextPairOne = rules[pairOfLetters][0]
        #print(f"Using rule {rules[pairOfLetters]}")
        newTemplate[nextPairOne] = (newTemplate[nextPairOne] + template[pairOfLetters]) if nextPairOne in newTemplate else template[pairOfLetters]
        #print(f"Value of {nextPairOne} in next step will be {newTemplate[nextPairOne]}")

        nextPairTwo = rules[pairOfLetters][1]
        #print(f"Using rule {rules[pairOfLetters]}")
        newTemplate[nextPairTwo] = (newTemplate[nextPairTwo] + template[pairOfLetters]) if nextPairTwo in newTemplate else template[pairOfLetters]
        #print(f"Value of {nextPairTwo} in next step will be {newTemplate[nextPairTwo]}")
        #print("")
    return newTemplate

#TODO - include first and last letter, divide by 2
def getLetterCounts(template):
    letterCounts = dict()
    for pair in template:
        letterCounts[pair[0]] = (template[pair] + letterCounts[pair[0]]) if pair[0] in letterCounts else template[pair]
        letterCounts[pair[1]] = (template[pair] + letterCounts[pair[1]]) if pair[1] in letterCounts else template[pair]
    letterCounts[firstLetter] += 1
    letterCounts[lastLetter] += 1
    return {key: val/2 for key, val in letterCounts.items()}

for _ in range(40):
    template = doStep(template)
    print(getLetterCounts(template))

lCount = sorted(getLetterCounts(template).items(), key = lambda x: x[1])
minimum, maximum = lCount[0][1], lCount[-1][1]
print(f"Result is {maximum - minimum= }")