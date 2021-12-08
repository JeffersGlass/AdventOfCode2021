from dataclasses import dataclass

@dataclass
class displayRun:
    hookups: list[str]
    outputs: list[str]

with open("input.txt", "r", encoding="utf-8") as infile:
    runs = [displayRun(hookups = line.split('|')[0].strip().split(" "), outputs = line.split('|')[1].strip().split(" ")) for line in infile.read().split('\n')]

sum = 0
for r in runs:
    for o in r.outputs:
        if len(o) in [2, 3, 4, 7]: sum+=1

print(f"{sum=}")