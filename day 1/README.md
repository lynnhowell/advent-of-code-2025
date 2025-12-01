# Advent of Code 2025 - Day 1

Solution for [Advent of Code 2025 Day 1](https://adventofcode.com/2025/day/1)

## Files

- `solve_safe.py` - Python script that solves both Part 1 and Part 2 of the puzzle
- `input.txt` - Your puzzle input data

## Setup

### Input File Location

The `input.txt` file must be placed **in the same directory** as the `solve_safe.py` script (i.e., in the `day 1` folder).

```
day 1/
├── README.md
├── solve_safe.py
└── input.txt          # <-- Input file goes here
```

### Getting Your Puzzle Input

1. Go to https://adventofcode.com/2025/day/1
2. Log in to your Advent of Code account
3. Copy your personalized puzzle input
4. Paste it into the `input.txt` file

## How to Run

Make sure you're in the `day 1` directory, then run:

```bash
python3 solve_safe.py
```

Or if the script is executable:

```bash
./solve_safe.py
```

## Expected Output

The script will output solutions for both parts:

```
Part 1 (end-of-rotation zeros) password: <answer>
Part 2 (any-click zeros, method 0x434C49434B) password: <answer>
```

## What the Script Does

The solution simulates a circular dial puzzle:
- **Part 1**: Counts how many times the dial lands on position 0 after completing each rotation
- **Part 2**: Counts how many times the dial passes through position 0 during all rotations (including intermediate clicks)

The dial has 100 positions (0-99), starts at position 50, and processes Left (L) and Right (R) rotation instructions from the input.
