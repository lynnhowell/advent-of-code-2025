# Advent of Code 2025 - Day 1: Safe Dial Solver

This script solves the Advent of Code 2025 Day 1 puzzle, which involves simulating the rotation of a safe's dial according to a list of instructions. The goal is to determine how many times the dial aligns to position `0`, under two different counting methods.

## File Structure

- `solve_safe.py` — Main solution script for Day 1.
- `input.txt` — Place your Day 1 puzzle input here.

## How It Works

### 1. Parsing Instructions

The script reads each line from `input.txt` and only keeps lines that start with `L` (left) or `R` (right) followed by a number. Any story text or blank lines are ignored to extract just the rotation instructions.

### 2. Part 1: End-of-Rotation Zeros

The function `count_zero_positions_end_only` counts how many times the safe dial lands exactly at position `0` **after** completing the rotation described in each instruction.

- The dial starts at position `50` (customizable).
- Each instruction rotates the dial left or right by a given number of positions.
- Only the final position after each instruction is considered for counting zeros.

### 3. Part 2: Any-Click Zeros (`method 0x434C49434B`)

The function `count_zero_positions_any_click` counts how many times **any click** (including all intermediary positions during a rotation) causes the dial to be at position `0`.

- The dial starts at position `50` (customizable).
- For each instruction, it calculates how many times passing through positions (right or left) aligns exactly at `0` using arithmetic for efficiency rather than step-by-step simulation.

### 4. Output

The script prints:

```
Part 1 (end-of-rotation zeros) password: <number>
Part 2 (any-click zeros, method 0x434C49434B) password: <number>
```

## Usage

1. Put your puzzle input into a file called `input.txt` in the same directory as `solve_safe.py`.
2. Run the script:

```bash
python3 solve_safe.py
```

## Functions

- `parse_instructions(lines)`: Parses puzzle input to extract valid rotation instructions.
- `count_zero_positions_end_only(instructions, start, modulus)`: Part 1 zero counter.
- `count_zero_positions_any_click(instructions, start, modulus)`: Part 2 zero counter (counts all clicks).

## Customization

- Starting position (`start`) and dial modulus (`modulus`, default 100) can be changed as needed by editing the script.

## License

This repository is for educational purposes as part of Advent of Code 2025.
