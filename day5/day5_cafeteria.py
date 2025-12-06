filename = "input5.txt"

with open(filename, "r") as f:
    list_of_lines = f.readlines()

blank_line_index = list_of_lines.index("\n")

id_ranges = [line.strip().split("-") for line in list_of_lines[0:blank_line_index]]
ingredient_ids = [int(line.strip()) for line in list_of_lines[blank_line_index + 1 :]]

counter = 0
for ingredient_id in ingredient_ids:
    for id_range in id_ranges:
        if int(id_range[0]) <= ingredient_id <= int(id_range[1]):
            counter += 1
            break

print(counter)
