from itertools import combinations


def main():
    lines = read_puzzle()

    containers = [int(line) for line in lines]
    combinations = get_combinations(containers, 150)

    print(combinations)


def get_combinations(containers, target):
    containers_combinations = [
        (comb, i)
        for i in range(1, len(containers) + 1)
        for comb in combinations(containers, i)
        if sum(comb) == target
    ]

    min_containers = min([comb[1] for comb in containers_combinations])

    return len([comb for comb in containers_combinations if comb[1] == min_containers])


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
