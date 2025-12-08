JunctionList = []
with open("input8.txt", "r") as data:
    for t in data:
        Line = t.strip()
        A,B,C = Line.split(",")
        JunctionList.append((int(A), int(B), int(C)))

JunctionInDict = {}
AdjacenciesList = []
NumJunctions = len(JunctionList)
for va in range(NumJunctions):
    JunctionInDict[va] = None
    AX, AY, AZ = JunctionList[va]
    for vb in range(va+1, NumJunctions):
        BX, BY, BZ = JunctionList[vb]
        Distance = (AX-BX)**2 + (AY-BY)**2 + (AZ-BZ)**2
        AdjacenciesList.append((Distance, va, vb))

def Part1Parse():
    CircuitSizes = []
    for y in CircuitDict:
        Size = len(CircuitDict[y])
        CircuitSizes.append(Size)
    CircuitSizes.sort()
    CircuitSizes.reverse()
    Answer = CircuitSizes[0]*CircuitSizes[1]*CircuitSizes[2]
    return Answer


AdjacenciesList.sort()
CircuitDict = {}
CurrentCircuit = 1
for t in range(len(AdjacenciesList)):
    _, A, B = AdjacenciesList[t]
    CA = JunctionInDict[A]
    CB = JunctionInDict[B]
    if CA == CB == None:
        CircuitDict[CurrentCircuit] = set()
        CircuitDict[CurrentCircuit].add(A)
        CircuitDict[CurrentCircuit].add(B)
        JunctionInDict[A] = CurrentCircuit
        JunctionInDict[B] = CurrentCircuit
        CurrentCircuit += 1
    elif CA == CB:
        continue
    elif CA == None:
        CircuitDict[CB].add(A)
        JunctionInDict[A] = CB
    elif CB == None:
        CircuitDict[CA].add(B)
        JunctionInDict[B] = CA
    else:
        CircuitDict[CA] = CircuitDict[CA] | CircuitDict[CB]
        del CircuitDict[CB]
        for j in CircuitDict[CA]:
            JunctionInDict[j] = CA
    
    if t == 999:
        Part1Answer = Part1Parse()
    Stop = False
    for u in [CA, CB]:
        if u not in CircuitDict:
            continue
        if len(CircuitDict[u]) == NumJunctions:
            AX = JunctionList[A][0]
            AB = JunctionList[B][0]
            Part2Answer = AX*AB
            Stop = True
            break
    if Stop:
        break


print(f"{Part1Answer = }")
print(f"{Part2Answer = }")
