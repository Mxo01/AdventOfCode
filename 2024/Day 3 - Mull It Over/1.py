import re


def main():
    lines = read_puzzle()

    mul_sum = 0

    for line in lines:
        mul_sum += sum(
            map(
                multiply,
                re.findall(r"mul\(\d+,\d+\)", line),
            )
        )

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
