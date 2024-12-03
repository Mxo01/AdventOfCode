def main():
    safe_reports_count = 0

    f = open("puzzle.txt", "r")

    for line in f:
        line = list(map(int, line.split(" ")))

        if is_line_safe(line):
            safe_reports_count += 1
            
    f.close()

    print(safe_reports_count)


def is_line_safe(line):
    return is_sorted(line) and are_all_levels_safe(line)


def is_sorted(line):
    return sorted(line) == line or sorted(line, reverse=True) == line

def are_all_levels_safe(line):
    return all(
        1 <= abs(int(line[i]) - int(line[i + 1])) <= 3 for i in range(len(line) - 1)
    )


if __name__ == "__main__":
    main()
