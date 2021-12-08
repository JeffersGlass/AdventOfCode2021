from dataclasses import dataclass

@dataclass
class displayRun:
    hookups: list[str]
    outputs: list[str]

with open("input.txt", "r", encoding="utf-8") as infile:
    runs = [displayRun(hookups = line.split('|')[0].strip().split(" "), outputs = line.split('|')[1].strip().split(" ")) for line in infile.read().split('\n')]

totalUnique = sum([sum([(1 if len(segments) in [2,3,4,7] else 0) for segments in r.outputs]) for r in runs])
print(f"{totalUnique=}")