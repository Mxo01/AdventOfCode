import re

def main():
    lines = read_puzzle()

    xmas_count = 0

    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] != "A":
                continue

            top_left = lines[i - 1][j - 1] if i > 0 and j > 0 else ""
            top_right = lines[i - 1][j + 1] if i > 0 and j < len(lines) - 1 else ""
            bottom_left = lines[i + 1][j - 1] if i < len(lines) - 1 and j > 0 else ""
            bottom_right = lines[i + 1][j + 1] if i < len(lines) - 1 and j < len(lines) - 1 else ""

            left_diag = top_left + lines[i][j] + bottom_right
            right_diag = top_right + lines[i][j] + bottom_left

            if re.match(r"MAS|SAM", left_diag) and re.match(r"MAS|SAM", right_diag):
                xmas_count += 1

    print(xmas_count)

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines

if __name__ == '__main__':
	main()
