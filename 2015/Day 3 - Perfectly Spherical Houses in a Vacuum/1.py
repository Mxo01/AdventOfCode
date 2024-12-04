def main():
    lines = read_puzzle()

    visited = set()
    visited.add((0, 0))
    x, y = 0, 0

    for line in lines:
        for direction in line:
            x += 1 if direction == ">" else -1 if direction == "<" else 0
            y += 1 if direction == "^" else -1 if direction == "v" else 0

            visited.add((x, y))

    print(len(visited))


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
