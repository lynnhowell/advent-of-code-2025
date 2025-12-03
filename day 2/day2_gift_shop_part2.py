#!/usr/bin/env python3

"""
Day 2: Gift Shop – Part Two

An ID is invalid if its decimal representation consists of some sequence
of digits repeated at least twice.

Examples:
- "123123"  (base "123", repeated 2 times)
- "121212"  (base "12", 3 times)
- "1111111" (base "1", 7 times)

This script:
- Parses the given ranges.
- Generates all such repeated-pattern numbers within the global min/max.
- Filters them by the ranges.
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


def generate_invalid_numbers(global_min, global_max):
    """
    Generate all numbers N in [global_min, global_max] such that
    N's decimal representation is some block of digits repeated
    k times, where k >= 2.

    We do this by digit-length:

      Let total digits = n.
      Let base block length = d, where d divides n and n/d = k >= 2.
      Let A be the base block (d digits, no leading zero).
      Then N = int(str(A) repeated k times).

    We enumerate all (n, d, A) combinations and keep N within [global_min, global_max].
    To avoid duplicates (e.g. 111111 can be many patterns), we store in a set.
    """
    invalid = set()
    max_digits = len(str(global_max))

    for n in range(2, max_digits + 1):  # total number of digits
        for d in range(1, n // 2 + 1):
            if n % d != 0:
                continue
            k = n // d
            if k < 2:
                continue

            # A is a d-digit number with no leading zero
            start = 10 ** (d - 1)
            end = 10 ** d

            for A in range(start, end):
                s = str(A) * k
                N = int(s)

                if N < global_min:
                    continue
                if N > global_max:
                    # For fixed d,k, N increases with A, so we can stop this loop.
                    break

                invalid.add(N)

    
    return invalid


def sum_invalid_ids_in_ranges(ranges):
    """
    For the given list of ranges, compute the sum of all invalid IDs
    that lie within any of those ranges.
    """
    global_min = min(start for start, end in ranges)
    global_max = max(end for start, end in ranges)

    invalid_numbers = generate_invalid_numbers(global_min, global_max)

    total = 0
    for n in invalid_numbers:
        for L, R in ranges:
            if L <= n <= R:
                total += n
                break

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
    total = sum_invalid_ids_in_ranges(ranges)

    print(f"Sum of all invalid IDs (Part 2 rules): {total}")


if __name__ == "__main__":
    main()
