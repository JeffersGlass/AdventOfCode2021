from dataclasses import dataclass

@dataclass(kw_only=True)
class displayRun:
    hookups: list[str]
    outputs: list[str]
    segmentAssigns : dict[str:str](default_factory=dict)

with open("input.txt", "r", encoding="utf-8") as infile:
    runs = [displayRun(hookups = line.split('|')[0].strip().split(" "), outputs = line.split('|')[1].strip().split(" "), segmentAssigns = dict()) for line in infile.read().split('\n')]

def numFromSegmentsOn(segmentsOn):
    sortedLetters = ''.join(sorted([letter for letter in segmentsOn]))
    if  sortedLetters == 'abcefg'   : return 0
    if  sortedLetters == 'cf'       : return 1   
    if  sortedLetters == 'acdeg'    : return 2  
    if  sortedLetters == 'acdfg'    : return 3  
    if  sortedLetters == 'bcdf'     : return 4  
    if  sortedLetters == 'abdfg'    : return 5  
    if  sortedLetters == 'abdefg'   : return 6  
    if  sortedLetters == 'acf'      : return 7
    if  sortedLetters == 'abcdefg'  : return 8  
    if  sortedLetters == 'abcdfg'   : return 9

    raise ValueError(f"Sorted letters {sortedLetters} do not match any digit pattern")


sum = 0 
for r in runs:
    #Determine display: control wire mapping
    #{"actual illuminated output: wire that currently controls it"}
    hookupsWithLen = dict()
    for i in range(2, 7+1):
        hookupsWithLen[i] = [h for h in r.hookups if len(h) == i]

    r.segmentAssigns['a'] = [seg for seg in 'abcdefg' if (seg in hookupsWithLen[3][0] and seg not in hookupsWithLen[2][0])][0] #know wiring of segment a]

    d_or_g = [seg for seg in 'abcdefg' if (len([h for h in hookupsWithLen[5] if seg in h]) == 3 and seg != r.segmentAssigns['a'])] #based on hookups with 5 segments 
    r.segmentAssigns['d'] = [seg for seg in 'abcdefg' if seg in d_or_g and seg in hookupsWithLen[4][0]][0] #based on single length-4 hookup
    r.segmentAssigns['g'] = [seg for seg in 'abcdefg' if seg in d_or_g and seg != r.segmentAssigns['d']][0]


    b_or_e = [seg for seg in 'abcdefg' if len([h for h in hookupsWithLen[5] if seg in h]) == 1] #based on hookups with 5 segments on
    r.segmentAssigns['e'] = [seg for seg in 'abcdefg' if seg in b_or_e and len([h for h in hookupsWithLen[6] if seg in h]) == 2][0] #based on hookups with 5 segments and knowing 'b' already
    r.segmentAssigns['b'] = [seg for seg in 'abcdefg' if seg in b_or_e and seg != r.segmentAssigns['e']][0]


    c_or_f = [seg for seg in 'abcdefg' if len([h for h in hookupsWithLen[5] if seg in h]) == 2] #based on hookups with 5 segments on
    r.segmentAssigns['c'] = [seg for seg in 'abcdefg' if seg in c_or_f and len([h for h in hookupsWithLen[6] if seg in h]) == 2][0]
    r.segmentAssigns['f'] = [seg for seg in 'abcdefg' if seg in c_or_f and seg != r.segmentAssigns['c']][0]

    #print(r)
    #print("---Segment Mapping---")
    #print("Scrambled Numbers: abcdefg")
    #print("Actual Digits:     ", end = "")
    #for letter in "abcdefg":
    #    print([l for l in 'abcdefg' if r.segmentAssigns[l] == letter][0], end = "")
    #print("")
    #print("Output Digits:") 
    rowSum = 0
    for i, digit in enumerate(r.outputs):
        #print(f">---\tDigit with messed up wiring: {digit}")
        rewiredDigit = ''.join([seg for seg in 'abcdefg' if r.segmentAssigns[seg] in digit])
        rewiredNum = numFromSegmentsOn(rewiredDigit)
        rowSum += rewiredNum * 10 ** (3-i)
        #print(f"\tCorrected digit: {rewiredDigit}")
        #print(f"\tCorresponding number: {numFromSegmentsOn(rewiredDigit)}")
    #print("")
    sum += rowSum

print(f"Total of all rewired numbers: {sum}")











""" 
NumSegments     Digits      Notes
2               1           
3               7
4               4
5               2,3,5       segcounts: 1(b, e)      2(c, f)      3(a, d, g)
6               0,6,9       segcounts:              2(c, d, e)         3(a, b, f, g)
7               8
    """