def main():
    line = read_puzzle()[0]

    rearranged_string = rearrange_string(line)
    compacted_string = compact_string(rearranged_string)

    print(sum(i * int(compacted_string[i]) for i in range(len(compacted_string))))


def rearrange_string(line):
    rearranged_string = []
    current_file_id = 0

    for current_index in range(len(line)):
        for _ in range(int(line[current_index])):
            rearranged_string.append(
                "." if current_index % 2 != 0 else str(current_file_id)
            )

        if not current_index % 2 == 0:
            current_file_id += 1

    return rearranged_string


def compact_string(rearranged_string):
    compacted_string = []
    start_index = 0
    end_index = len(rearranged_string) - 1

    while start_index <= end_index:
        while start_index < end_index and rearranged_string[end_index] == ".":
            end_index -= 1

        if rearranged_string[start_index] == ".":
            compacted_string.append(rearranged_string[end_index])
            start_index += 1
            end_index -= 1
        else:
            compacted_string.append(rearranged_string[start_index])
            start_index += 1

    return compacted_string


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
