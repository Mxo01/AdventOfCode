def main():
    lines = read_puzzle()

    empty_line_index = lines.index("")
    rules = lines[:empty_line_index]
    updates = list(map(lambda update: update.split(","), lines[empty_line_index + 1:]))
    middle_pages_sum = sum(int(update[len(update) // 2]) if is_update_correct(update, rules) else 0 for update in updates)

    print(middle_pages_sum)

def is_update_correct(update, rules):
    return all(update[i] + "|" + update[i + 1] in rules for i in range(len(update) - 1))

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines

if __name__ == '__main__':
	main()
