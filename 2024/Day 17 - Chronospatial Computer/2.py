def main():
    lines = read_puzzle()

    program = parse_puzzle(lines)

    a_values = []

    for a in range(8):
        find_lowest_a_registry(a, program, a_values)

    print(min(a_values))


def parse_puzzle(lines):
    program = []

    for line in lines:
        if not "Program" in line:
            continue
        else:
            program = list(map(int, line.split(": ")[1].split(",")))

    return program


def find_lowest_a_registry(a_registry, program, a_values, column=0):
    if execution_loop(a_registry) != program[-(column + 1)]:
        return

    if column == len(program) - 1:
        a_values.append(a_registry)
        return

    for b in range(8):
        find_lowest_a_registry((a_registry << 3) + b, program, a_values, column + 1)


def execution_loop(a_registry):
    b_registry = a_registry % 8
    b_registry = b_registry ^ 1
    c_registry = a_registry // 2**b_registry
    a_registry = a_registry // 2**3
    b_registry = b_registry ^ c_registry
    b_registry = b_registry ^ 6

    return b_registry % 8


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
