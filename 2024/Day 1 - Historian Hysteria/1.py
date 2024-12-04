def main():
    lines = read_puzzle()

    left = []
    right = []

    for line in lines:
        location_id_1 = int(line.split("   ")[0])
        location_id_2 = int(line.split("   ")[1])
        left.append(location_id_1)
        right.append(location_id_2)

    left = sorted(left)
    right = sorted(right)

    total_distance = sum(abs(left[pos] - right[pos]) for pos in range(len(left)))

    print(total_distance)


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
