def main():
    lines = read_puzzle()

    empty_line_index = lines.index("")
    rules = lines[:empty_line_index]
    updates = list(map(lambda update: update.split(","), lines[empty_line_index + 1:]))
    middle_pages_sum = sum(int(update[len(update) // 2]) for update in updates_to_sum(updates, rules))

    print(middle_pages_sum)

def updates_to_sum(updates, rules):
    incorrect_updates = list(filter(lambda update: not is_update_correct(update, rules), updates))

    for incorrect_update in incorrect_updates:
        i = 0

        while True:
            if i == len(incorrect_update) - 1:
                if is_update_correct(incorrect_update, rules):
                    break

                i = 0

            if not incorrect_update[i] + "|" + incorrect_update[i + 1] in rules:
                incorrect_update[i], incorrect_update[i + 1] = incorrect_update[i + 1], incorrect_update[i]

            i += 1


    return incorrect_updates

def is_update_correct(update, rules):
    return all(update[i] + "|" + update[i + 1] in rules for i in range(len(update) - 1))

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines

if __name__ == '__main__':
	main()
