import re

def main():
    lines = read_puzzle()

    xmas_count = 0

    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] != "X":
                continue

            top = lines[i][j] + lines[i - 1][j] + lines[i - 2][j] + lines[i - 3][j] if i >= 3 else ""
            top_right = lines[i][j] + lines[i - 1][j + 1] + lines[i - 2][j + 2] + lines[i - 3][j + 3] if i >= 3 and j <= len(lines) - 4 else ""
            right = lines[i][j] + lines[i][j + 1] + lines[i][j + 2] + lines[i][j + 3] if j <= len(lines) - 4 else ""
            bottom_right = lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2] + lines[i + 3][j + 3] if i <= len(lines) - 4 and j <= len(lines) - 4 else ""
            bottom = lines[i][j] + lines[i + 1][j] + lines[i + 2][j] + lines[i + 3][j] if i <= len(lines) - 4 else ""
            bottom_left = lines[i][j] + lines[i + 1][j - 1] + lines[i + 2][j - 2] + lines[i + 3][j - 3] if i <= len(lines) - 4 and j >= 3 else ""
            left = lines[i][j] + lines[i][j - 1] + lines[i][j - 2] + lines[i][j - 3] if j >= 3 else ""
            top_left = lines[i][j] + lines[i - 1][j - 1] + lines[i - 2][j - 2] + lines[i - 3][j - 3] if i >= 3 and j >= 3 else ""

            xmas_count += len(list(filter(lambda match: re.match(r"XMAS", match), [top, top_right, right, bottom_right, bottom, bottom_left, left, top_left])))

    print(xmas_count)

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines

if __name__ == '__main__':
	main()
