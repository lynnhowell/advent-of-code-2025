#!/usr/bin/env python3

def parse_instructions(lines):
    """
    Parse the puzzle input lines.
    Keeps only lines that start with 'L' or 'R' followed by a number.
    Ignores any story text or blank lines.
    """
    instructions = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue

        # Only treat lines starting with L/R + digits as instructions
        if line[0] in ("L", "R"):
            # Some lines might have trailing text, e.g. "R25 - The Elves..."
            dir_char = line[0]
            num_str = ""
            for ch in line[1:]:
                if ch.isdigit():
                    num_str += ch
                else:
                    break

            if num_str:
                instructions.append(dir_char + num_str)

    return instructions


def count_zero_positions_end_only(instructions, start=50, modulus=100):
    """
    Part One:
    Count how many times the dial is at 0 *after* a rotation.
    """
    pos = start
    count_zero = 0

    for instr in instructions:
        direction = instr[0]
        steps = int(instr[1:])

        if direction == "L":
            pos = (pos - steps) % modulus
        elif direction == "R":
            pos = (pos + steps) % modulus
        else:
            raise ValueError(f"Unknown direction in instruction: {instr}")

        if pos == 0:
            count_zero += 1

    return count_zero


def count_zero_positions_any_click(instructions, start=50, modulus=100):
    """
    Part Two (method 0x434C49434B):
    Count how many times ANY CLICK lands on 0, including intermediate
    positions during a rotation.

    For each rotation, we don't simulate every step; we use arithmetic:

    - Right (R): positions visited are s+1, ..., s+steps (mod modulus).
      0 is hit when s + j ≡ 0 (mod modulus) for some j in [1, steps].

    - Left (L): positions visited are s-1, ..., s-steps (mod modulus).
      0 is hit when s - j ≡ 0 (mod modulus) for some j in [1, steps].
    """
    pos = start
    count_total = 0

    for instr in instructions:
        direction = instr[0]
        steps = int(instr[1:])

        if direction == "R":
            # First j >= 1 such that (pos + j) % modulus == 0
            if pos != 0:
                j0 = (modulus - pos) % modulus
                if j0 == 0:
                    j0 = modulus
            else:
                # If starting at 0, the first time we see 0 again is after modulus steps
                j0 = modulus

            if j0 <= steps:
                # One hit at j0, plus more every full turn of modulus
                count_total += 1 + (steps - j0) // modulus

            # Update final position
            pos = (pos + steps) % modulus

        elif direction == "L":
            # First j >= 1 such that (pos - j) % modulus == 0
            if pos != 0:
                j0 = pos % modulus  # j0 in [1..modulus-1]
                if j0 <= steps:
                    count_total += 1 + (steps - j0) // modulus
            # If pos == 0, moving left never passes through 0 again in that rotation

            # Update final position
            pos = (pos - steps) % modulus

        else:
            raise ValueError(f"Unknown direction in instruction: {instr}")

    return count_total


def main():
    # Read your puzzle input from input.txt
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    instructions = parse_instructions(lines)

    part1 = count_zero_positions_end_only(instructions, start=50, modulus=100)
    part2 = count_zero_positions_any_click(instructions, start=50, modulus=100)

    print(f"Part 1 (end-of-rotation zeros) password: {part1}")
    print(f"Part 2 (any-click zeros, method 0x434C49434B) password: {part2}")


if __name__ == "__main__":
    main()