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
    return len([design for design in designs if is_design_possible(towels, design, {})])


def is_design_possible(towels, design, memo):
    if not design:
        return True

    if design in memo:
        return memo[design]

    for towel in towels:
        if design.startswith(towel):
            if is_design_possible(towels, design[len(towel) :], memo):
                memo[design] = True
                return True

    memo[design] = False

    return False


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
