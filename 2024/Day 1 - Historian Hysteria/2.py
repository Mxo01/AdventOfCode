def main():
    lines = read_puzzle()

    list1 = []
    list2 = []
    similarity_score = 0

    for line in lines:
        location_id_1 = int(line.split("   ")[0])
        location_id_2 = int(line.split("   ")[1])
        list1.append(location_id_1)
        list2.append(location_id_2)

    similarity_score = sum(
        list1[pos] * list2.count(list1[pos]) for pos in range(len(list1))
    )

    print(similarity_score)


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.readlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
