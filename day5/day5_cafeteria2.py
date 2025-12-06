filename = "input5.txt"

with open(filename, "r") as f:
    list_of_lines = f.readlines()
blank_line_index = list_of_lines.index("\n")

id_ranges = [
    (int(id_range[0]), int(id_range[1]))
    for id_range in [
        line.strip().split("-") for line in list_of_lines[0:blank_line_index]
    ]
]

range_starts = [id_range[0] for id_range in id_ranges]
range_ends = [id_range[1] for id_range in id_ranges]

for id_range_a in id_ranges:
    for id_range_b in id_ranges:
        if id_range_b[0] < id_range_a[0] <= id_range_b[1] + 1:
            range_starts.remove(id_range_a[0])
            break

for id_range_a in id_ranges:
    for id_range_b in id_ranges:
        if id_range_b[0] - 1 <= id_range_a[1] < id_range_b[1]:
            range_ends.remove(id_range_a[1])
            break

unique_range_starts = set(range_starts)
unique_range_ends = set(range_ends)

print(sum(unique_range_ends) - sum(unique_range_starts) + len(unique_range_starts))
