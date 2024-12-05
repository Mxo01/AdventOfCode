def main():
    lines = read_puzzle()
    print(sum(1 if has_pair_that_appears_twice(line) and has_two_equal_with_one_between(line) else 0 for line in lines))


def has_pair_that_appears_twice(line):
    return any(line[i] + line[i + 1] in line[i+2:] for i in range(len(line) - 1))


def has_two_equal_with_one_between(line):
    return any(line[i] == line[i + 2] for i in range(len(line) - 2))

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
