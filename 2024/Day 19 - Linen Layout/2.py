def main():
    lines = read_puzzle()

    towels, designs = parse_puzzle(lines)
    possible_designs = get_possible_designs(towels, designs)

    print(possible_designs)


def parse_puzzle(lines):
    towels, designs = [], []
    empty_line_encountered = False

    for line in lines:
        if line.strip() == "":
            empty_line_encountered = True
        elif not empty_line_encountered:
            towels = list(line.split(", "))
        else:
            designs.append(line)

    return towels, designs


def get_possible_designs(towels, designs):
    return sum([count_possible_designs(towels, design, {}) for design in designs])


def count_possible_designs(towels, design, memo):
    if not design:
        return 1

    if design in memo:
        return memo[design]

    combinations = 0

    for towel in towels:
        if design.startswith(towel):
            combinations += count_possible_designs(towels, design[len(towel) :], memo)

    memo[design] = combinations

    return combinations


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
