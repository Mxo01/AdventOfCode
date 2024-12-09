def main():
    line = read_puzzle()[0]

    rearranged_string = rearrange_string(line)
    compacted_string = compact_string(rearranged_string)

    print(
        sum(
            i * int(char) if char != "." else 0
            for i, char in enumerate(flat(compacted_string))
        )
    )


def rearrange_string(line):
    rearranged_string = []
    current_file_id = 0

    for current_index in range(len(line)):
        substr = []

        for _ in range(int(line[current_index])):
            substr.append("." if current_index % 2 != 0 else str(current_file_id))

        if len(substr) > 0:
            rearranged_string.append(substr)

        if not current_index % 2 == 0:
            current_file_id += 1

    return rearranged_string


def compact_string(rearranged_string):
    start_index = 0
    end_index = len(rearranged_string) - 1

    while start_index <= end_index:
        if "." in rearranged_string[start_index]:
            current_index_length = rearranged_string[start_index].count(".")
            internal_end_index = end_index
            file_to_move_found = False

            while start_index <= internal_end_index:
                if "." in rearranged_string[internal_end_index]:
                    internal_end_index -= 1
                    continue

                end_index_length = len(rearranged_string[internal_end_index])

                if end_index_length <= current_index_length:
                    file_to_move_found = True

                    rearranged_string[start_index] = (
                        list(
                            filter(
                                lambda char: char != ".", rearranged_string[start_index]
                            )
                        )
                        + rearranged_string[internal_end_index]
                        + ["." for _ in range(current_index_length - end_index_length)]
                    )

                    rearranged_string[internal_end_index] = [
                        "." for _ in range(end_index_length)
                    ]

                    break

                internal_end_index -= 1

            if not file_to_move_found:
                start_index += 1
        else:
            start_index += 1

    return rearranged_string


def flat(compacted_string):
    return [char for sublist in compacted_string for char in sublist]


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
