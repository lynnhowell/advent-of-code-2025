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
        "52500467-52574194,655624494-655688785,551225-576932,"
        "8418349387-8418411293,678-1464,33-79,74691-118637,"
        "8787869169-8787890635,9898977468-9899009083,548472423-548598890,"
        "337245835-337375280,482823-543075,926266-991539,1642682920-1642753675,"
        "3834997-3940764,1519-2653,39697698-39890329,3-21,3251796-3429874,"
        "3467-9298,26220798-26290827,80-124,200638-280634,666386-710754,"
        "21329-64315,250-528,9202893-9264498,819775-903385,292490-356024,"
        "22-32,2663033-2791382,133-239,56514707-56704320,432810-458773,"
        "4949427889-4949576808"
    )

    ranges = parse_ranges(ranges_str)
    total = sum_invalid_ids(ranges)

    print(f"Sum of all invalid IDs: {total}")


if __name__ == "__main__":
    main()