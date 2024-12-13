import numpy as np
import re


def main():
    lines = read_puzzle()

    claws = get_claws(lines)
    tokens = calculate_tokens(claws)

    print(tokens)


def get_claws(lines):
    number_of_claws = len(list(filter(lambda line: line.strip() == "", lines))) + 1
    claws = [[] for _ in range(number_of_claws)]
    current_claw = 0

    for line in lines:
        if line.strip() == "":
            current_claw += 1
        else:
            claws[current_claw].append(extract_claw_data(line))

    return claws


def extract_claw_data(line):
    return list(map(int, re.findall(r"\d+", line)))


def calculate_tokens(claws):
    tokens = []

    for claw in claws:
        button_a, button_b, prize = claw
        eq_1 = np.array([[button_a[0], button_b[0]], [button_a[1], button_b[1]]])
        result = np.array([10000000000000 + prize[0], 10000000000000 + prize[1]])
        solutions = np.linalg.solve(eq_1, result)
        rounded_solutions = np.round(solutions)

        if (
            np.all(rounded_solutions >= 0)
            and np.allclose(solutions, rounded_solutions, rtol=1e-14)
        ):
            tokens.append(3 * solutions[0] + solutions[1])

    return int(sum(tokens))


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
