def main():
    print(sum([calculate_area(line) for line in read_puzzle()]))


def calculate_area(line):
    l, w, h = map(int, line.split("x"))
    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
