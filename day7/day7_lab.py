import numpy as np

"""
Part 1
"""

input_path = "inputs/07.txt"
# input_path = "inputs/07_example.txt"

with open(input_path) as file:
    input = file.readlines()
input = [list(x.replace("\n", "")) for x in input]

height = len(input)
width = len(input[0])

arr = np.array(input)

beams = np.array(arr[0, :] == "S", ndmin=2)
split_counter = 0
for row in range(height - 1):
    new_row = np.logical_and(beams[-1, :], arr[row + 1] != "^")
    splitter = np.logical_and(beams[-1, :], arr[row + 1] == "^")
    split_counter += sum(splitter)
    splitter_left = np.append(splitter[1:], np.array(False))
    splitter_right = np.append(np.array(False), splitter[:-1])
    new_row = np.logical_or.reduce((new_row, splitter_left, splitter_right))[
        np.newaxis, ...
    ]
    beams = np.append(beams, new_row, axis=0)


print(f"Result part 1: {split_counter}")

"""
Part 2
"""
arr = np.array(input)

beams = np.array(arr[0, :] == "S", ndmin=1, dtype=int)
for row in range(height - 1):
    new_beams = np.zeros(width, dtype=int)

    # pass through
    pass_through = np.where(np.logical_and(beams, arr[row + 1, :] != "^"))[0]
    for p in pass_through:
        new_beams[p] = beams[p]

    # splitter
    splitter = np.where(np.logical_and(beams, arr[row + 1] == "^"))[0]
    for s in splitter:
        new_beams[s - 1] += beams[s]
        new_beams[s + 1] += beams[s]
        new_beams[s] = 0

    beams = new_beams

timeline_counter = sum(beams)
print(f"Result part 2: {timeline_counter}")
