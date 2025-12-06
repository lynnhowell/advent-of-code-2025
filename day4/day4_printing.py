with open("input4.txt", "r") as puzzleInput:
    warehouse = [list(line.strip()) for line in puzzleInput]

rolls = set()
for y, row in enumerate(warehouse):
    for x, bin in enumerate(row):
        if bin == "@":
            rolls.add((x, y))

adjacents = [(-1,-1),(0, -1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
a1, a2, round, elves_working, removed = 0, 0, 0, True, set()

while elves_working:
    round += 1
    for x, y in rolls:
        adjacent_rolls = 0
        for dx, dy in adjacents:
            if (x + dx, y + dy) in rolls:
                adjacent_rolls += 1
            if adjacent_rolls > 3:
                break
        if adjacent_rolls < 4:
            removed.add((x, y))
    if removed:
        rolls -= removed
        if round == 1:
            a1 += len(removed)
        a2 += len(removed)
        removed.clear()
    else:
        elves_working = False

print(f"Part one: {a1} rolls removed")
print(f"Part two: {a2} rolls removed in {round} rounds of work")
