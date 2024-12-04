def main():
    print(sum([calculate_area(line) for line in read_puzzle()]))


def calculate_area(line):
    l, w, h = map(int, line.split("x"))
    return min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h) + l * w * h


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
