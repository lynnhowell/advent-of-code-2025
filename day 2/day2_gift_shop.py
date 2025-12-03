#!/usr/bin/env python3

"""
Day 2: Gift Shop – Invalid ID sum calculator

An ID is invalid if its decimal representation is made of some sequence
of digits repeated twice (e.g. 11, 6464, 123123).

This script:
- Parses the given ranges.
- Finds all such "double" numbers in those ranges.
- Sums them and prints the total.
"""

def parse_ranges(ranges_str):
    """
    Parse a comma-separated list of ranges like:
    "52500467-52574194,655624494-655688785,..."
    into a list of (start, end) integer tuples.
    """
    ranges = []
    for part in ranges_str.split(","):
        part = part.strip()
        if not part:
            continue
        a_str, b_str = part.split("-")
        ranges.append((int(a_str), int(b_str)))
    return ranges


def sum_invalid_ids(ranges):
    """
    Sum all invalid IDs in the given ranges.

    An invalid ID is a number whose decimal representation is AA,
    i.e. some non-empty sequence A repeated twice (no leading zeroes).
    We do this mathematically without iterating every number in the range.

    Any such number has an even number of digits: 2k.
    Let A be the first half, k digits, so:
        N = A * 10^k + A = A * (10^k + 1)

    For a given range [L, R], we solve for A:
        L <= A * (10^k + 1) <= R
    and restrict A to the k-digit range:
        10^(k-1) <= A <= 10^k - 1
    """
    total = 0

    # Find maximum number of digits needed across all ranges
    max_R = max(r[1] for r in ranges)
    max_digits = len(str(max_R))

    for L, R in ranges:
        # Consider only even digit lengths: 2, 4, 6, ...
        for digits in range(2, max_digits + 1, 2):
            k = digits // 2
            base = 10 ** k           # 10^k
            factor = base + 1        # (10^k + 1)

            # Solve L <= A * factor <= R  for A:
            # A >= ceil(L / factor)
            # A <= floor(R / factor)
            a_min = (L + factor - 1) // factor   # ceil division
            a_max = R // factor

            # Restrict A to k-digit numbers: [10^(k-1), 10^k - 1]
            a_min = max(a_min, 10 ** (k - 1))
            a_max = min(a_max, base - 1)

            if a_min > a_max:
                continue

            for A in range(a_min, a_max + 1):
                n = A * base + A
                # Extra safety check; should always be true if math above is correct
                if L <= n <= R:
                    total += n

    return total


def main():
    # Your puzzle input ranges as a single string:
    ranges_str = (
        "5529687-5587329,50-82,374-560,83-113,226375-287485,"
        "293169-368713,2034-2634,9945560-9993116,4872472-4904227,"
        "3218-5121,1074-1357,15451-26093,483468003-483498602,51513-85385,"
        "1466-1992,7600-13034,710570-789399,407363-480868,3996614725-3996662113,"
        "3-17,5414907798-5414992881,86274-120443,828669-909588,607353-700604,"
        "4242340614-4242556443,28750-44009,935177-1004747,20-41,74678832-74818251,"
        "8484825082-8484860878,2784096938-2784156610,5477-7589,621-952,"
        "2424167145-2424278200,147085-217900,93043740-93241586"

    )

    ranges = parse_ranges(ranges_str)
    total = sum_invalid_ids(ranges)

    print(f"Sum of all invalid IDs: {total}")


if __name__ == "__main__":
    main()
