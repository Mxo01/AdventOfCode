def main():
    lines = read_puzzle()
    print(sum(1 if has_vowels(line) and has_twice_in_a_row_char(line) and not has_unallowed_string(line) else 0 for line in lines))

def has_vowels(line):
    return sum(1 if char in ["a", "e", "i", "o", "u"] else 0 for char in line) >= 3

def has_twice_in_a_row_char(line):
    return any(line[i] == line[i + 1] for i in range(len(line) - 1))

def has_unallowed_string(line):
    return any(line[i] + line[i + 1] in ["ab", "cd", "pq", "xy"] for i in range(len(line) - 1))

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
