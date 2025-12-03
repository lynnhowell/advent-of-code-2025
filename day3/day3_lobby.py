# Advent of Code 2025 Day 3 Part 1 Solution
# Each line represents a bank of batteries with digits 1-9.
# For each bank, pick the two batteries (digits) that produce the largest possible "joltage" when concatenated.
# Sum the largest joltage from each bank as the answer.

def max_joltage(bank: str) -> int:
    # Consider all ordered pairs of distinct positions (i != j)
    max_val = -1
    n = len(bank)
    for i in range(n):
        for j in range(n):
            if i != j:
                val = int(bank[i] + bank[j])
                max_val = max(max_val, val)
    return max_val

def total_output(filename: str) -> int:
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                total += max_joltage(line)
    return total

if __name__ == '__main__':
    # Assuming input is in day3/day3part1.txt in the same repo
    input_file = 'input.txt'
    result = total_output(input_file)
    print(f'Total output joltage: {result}')
