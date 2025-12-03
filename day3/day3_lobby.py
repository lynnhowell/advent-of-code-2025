def max_pair_value(line):
    """
    Given a string of digits, find the maximum two-digit value formed by any two different digits.
    """
    digits = [int(c) for c in line.strip()]
    # Find the two largest digits
    first = max(digits)
    digits.remove(first)
    second = max(digits)
    return first * 10 + second

def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            if line.strip():
                total += max_pair_value(line)
    print(total)

if __name__ == "__main__":
    main()
