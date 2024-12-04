def main():
    lines = read_puzzle()

    safe_reports_count = 0

    for line in lines:
        line = list(map(int, line.split(" ")))
        safe_reports_count += (
            1
            if is_line_safe(line)
            or any(is_line_safe(line[:i] + line[i + 1 :]) for i in range(len(line)))
            else 0
        )

    print(safe_reports_count)


def is_line_safe(line):
    return is_sorted(line) and are_all_levels_safe(line)


def is_sorted(line):
    return sorted(line) == line or sorted(line, reverse=True) == line


def are_all_levels_safe(line):
    return all(
        1 <= abs(int(line[i]) - int(line[i + 1])) <= 3 for i in range(len(line) - 1)
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
