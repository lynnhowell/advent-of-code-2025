# Advent of Code 2025 - Day 2: Gift Shop

Solution for [Advent of Code 2025 Day 2](https://adventofcode.com/2025/day/2)

## Files

- `day2_gift_shop.py` - Solution for Part 1
- `day2_gift_shop_part2.py` - Solution for Part 2
- `input.txt` - Test input data
- `day2part1.txt` - Part 1 puzzle description
- `day2part2.txt` - Part 2 puzzle description

## Problem Overview

This puzzle involves finding "invalid" gift shop IDs based on their decimal representation:

### Part 1: Double Pattern
An ID is invalid if its decimal representation consists of some sequence of digits repeated **exactly twice**.

Examples:
- `11` (base "1" repeated 2 times)
- `6464` (base "64" repeated 2 times)
- `123123` (base "123" repeated 2 times)

### Part 2: Multiple Repetitions
An ID is invalid if its decimal representation consists of some sequence of digits repeated **at least twice** (2 or more times).

Examples:
- `123123` (base "123", repeated 2 times)
- `121212` (base "12", repeated 3 times)
- `1111111` (base "1", repeated 7 times)

## Setup

### File Structure

All files should be in the same directory:

```
day 2/
├── README.md
├── day2_gift_shop.py
├── day2_gift_shop_part2.py
├── input.txt
├── day2part1.txt
└── day2part2.txt
```

### Input Data

The puzzle input is **hardcoded** into both Python scripts as a series of number ranges. If you need to change the input:

1. Edit the `ranges_str` variable in the `main()` function of each script
2. Replace with your personalized puzzle input from Advent of Code

## How to Run

### Part 1 Solution

```bash
python3 day2_gift_shop.py
```

Or if executable:

```bash
./day2_gift_shop.py
```

### Part 2 Solution

```bash
python3 day2_gift_shop_part2.py
```

Or if executable:

```bash
./day2_gift_shop_part2.py
```

## Expected Output

### Part 1
```
Sum of all invalid IDs: <answer>
```

### Part 2
```
Sum of all invalid IDs (Part 2 rules): <answer>
```

## Algorithm Details

### Part 1 Algorithm
Uses mathematical optimization to find all numbers where the decimal representation is AA (some sequence A repeated twice). Instead of checking every number in the range, it:
- Calculates valid patterns based on digit length (must be even)
- Uses the formula: N = A × (10^k + 1), where k is half the digits
- Only generates valid candidates within the given ranges

### Part 2 Algorithm
Generates all numbers with repeated patterns by:
- Enumerating all possible base block lengths (d) and repetition counts (k ≥ 2)
- For each pattern length, generating all valid base numbers
- Creating the repeated pattern and checking if it falls within any range
- Using a set to avoid counting duplicates (e.g., "111111" can be many patterns)

Both algorithms efficiently handle large number ranges without iterating through every single number.
