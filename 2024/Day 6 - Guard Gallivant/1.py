def main():
    lines = read_puzzle()

    visited = set()
    x, y, direction = find_guard(lines)

    while True:
        visited.add((x, y))

        if should_stop(lines, x, y, direction):
            break

        next_x, next_y = update_position(x, y, direction)
        next = lines[next_x][next_y]

        if next == "#":
            direction = update_direction(direction)
            continue

        x, y = next_x, next_y

    print(len(visited))

def find_guard(lines):
    return next((i, line.index(symbol), direction) for i, line in enumerate(lines) for symbol, direction in {"^": "top", ">": "right", "v": "bottom", "<": "left"}.items() if symbol in line)

def should_stop(lines, x, y, direction):
    return x == 0 and direction == "top" or x == len(lines) - 1 and direction == "bottom" or y == 0 and direction == "left" or y == len(lines[x]) - 1 and direction == "right"

def update_direction(direction):
    return {"top": "right", "right": "bottom", "bottom": "left", "left": "top"}[direction]

def update_position(x, y, direction):
    return {"top": (x - 1, y), "right": (x, y + 1), "bottom": (x + 1, y), "left": (x, y - 1)}[direction]

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines

if __name__ == '__main__':
	main()
