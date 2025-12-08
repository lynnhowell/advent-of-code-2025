import sys
import math
from itertools import combinations

boxes = [tuple(map(int, line.split(','))) for line in sys.stdin]
P1 = 10 if len(boxes) < 50 else 1000

groups = {frozenset([b]) for b in boxes}
ds = sorted(combinations(boxes, 2), key=lambda p: math.dist(*p))

p1 = 0
for i, (p,q) in enumerate(ds):
    p2 = p[0]*q[0]
    g1, g2 = [next(g for g in groups if x in g) for x in (p, q)]
    groups -= {g1, g2}
    groups.add(g1 | g2)

    if i+1 == P1:
        p1 = math.prod(sorted(map(len, groups), reverse=True)[:3])

    if len(groups) == 1:
        break

print(p1, p2)
