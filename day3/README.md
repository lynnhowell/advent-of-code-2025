# Day 3 - Advent of Code 2025: Joltage Battery Analysis

This repository contains the solution for **Day 3** of Advent of Code 2025, implemented in Python. The challenge focuses on analyzing a series of battery banks to determine their "joltage output" using custom algorithms.

## Overview

- **Input:** Each line in `input.txt` represents a battery bank, consisting of digits. Each digit corresponds to a battery cell's energy value.
- **Part 1:** Finds the highest value (except the last cell), then concatenates the next highest value (after the highest) to form a "joltage" string for each battery. Sums up the total joltage across all batteries.
- **Part 2:** Extracts a "mega joltage" value by repeatedly finding and concatenating the largest remaining digit in a shrinking range, similar to a greedy selection process. Sums up the mega values across all batteries.

## Files

- `day3_lobby.py` — Main solution and parsing logic.
- `input.txt` — Challenge input data (placed in the same directory).

## Usage

1. **Install Python 3.7+** (and recommended: create a virtual environment).

2. **Prepare your input file.**

   Place your input as `input.txt` within the `day3/` directory, or use one of the example files by un-commenting in the script.

3. **Run the Script:**

   ```bash
   python day3_lobby.py
   ```

   Outputs will display the individual battery calculations and aggregate results for each part.

## Solution Functions

- **parse_input(data):**
  - Parses the input file into a list of lists of integers.

- **part1(parsed_data):**
  - For each battery bank, finds the highest and next highest digit (with order constraint), forms a joltage value, and prints/sums results.

- **part2(parsed_data):**
  - For each bank, constructs a "mega joltage" by greedily selecting max digits in successively reduced ranges. Prints and sums results.

## Example

Suppose your `input.txt` contains:

```
13579
24680
```

The script would process each row and print the detailed computation for each bank, followed by the total outputs.

## Custom Inputs

To run with different inputs:
- Create additional files in an `inputs/` subdirectory (e.g., `inputs/example1.txt`).
- Modify the `INPUT_PATH` in `day3_lobby.py` as needed by uncommenting the appropriate line.

## Contributing

Pull requests, improvements, and additional test inputs are welcome!

## License

[MIT](../LICENSE) (adjust depending on repo)

---

_Advent of Code © 2025 Eric Wastl. Solutions and input are for educational and discussion purposes only._
