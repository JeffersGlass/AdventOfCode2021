from collections import defaultdict
from collections import defaultdict

with open("input.txt", 'r') as infile:
    data = infile.read().split('\n')

numInputs = len(data)
onesCount = defaultdict(lambda: 0)

#Count the number of "1"'s at each digit position in all of the input numbers
for num in data:
    for i, digit in enumerate(num):
        onesCount[i] += int(digit)

#Calculate gamma, epison as lists of strings ("1" and "0")
gamma = [("1" if onesCount[i] > (numInputs / 2) else "0") for i in range(len(onesCount))]
epsilon = [("1" if gamma[i] == "0" else "0") for i in range(len(onesCount))]

#Concatenate lists, as 0b to represent binary, cast to int
result = int('0b' + ''.join(gamma), 2) * int('0b' + ''.join(epsilon), 2)
print(f"{gamma= } {epsilon= } {result= }")