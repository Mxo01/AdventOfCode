import re


def main():
    lines = read_puzzle()

    mul_sum = 0
    should_multiply = True

    for line in lines:
        matches = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)

        for match in matches:
            if match == "do()":
                should_multiply = True
                continue

            if match == "don't()":
                should_multiply = False
                continue

            if should_multiply:
                mul_sum += multiply(match)

    print(mul_sum)


def multiply(mul_str):
    left, right = re.findall(r"\d+", mul_str)
    return int(left) * int(right)


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
