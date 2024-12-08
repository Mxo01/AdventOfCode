def main():
    lines = read_puzzle()
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        from_coordinate, to_coordinate = [
            coordinate.strip() for coordinate in line.split("through")
        ]
        from_start, from_end = [
            int(index) for index in from_coordinate.split(" ")[-1].split(",")
        ]
        to_start, to_end = [int(index) for index in to_coordinate.split(",")]
        on, off = "turn on" in line, "turn off" in line

        for i in range(from_start, to_start + 1):
            for j in range(from_end, to_end + 1):
                grid[i][j] += 1 if on else (-1 if grid[i][j] > 0 else 0) if off else 2

    print(sum([sum(row) for row in grid]))


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
