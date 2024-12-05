from functools import cmp_to_key

def main():
    lines = read_puzzle()

    empty_line_index = lines.index("")
    rules = lines[:empty_line_index]
    updates = list(map(lambda update: update.split(","), lines[empty_line_index + 1:]))
    middle_pages_sum = sum(int(update[len(update) // 2]) for update in updates_to_sum(updates, rules))

    print(middle_pages_sum)

def updates_to_sum(updates, rules):
    return list(map(lambda incorrect_update: sorted(incorrect_update, key=cmp_to_key(lambda page1, page2: 1 if page1 + "|" + page2 in rules else -1)), list(filter(lambda update: not is_update_correct(update, rules), updates))))

def is_update_correct(update, rules):
    return all(update[i] + "|" + update[i + 1] in rules for i in range(len(update) - 1))

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines

if __name__ == '__main__':
	main()