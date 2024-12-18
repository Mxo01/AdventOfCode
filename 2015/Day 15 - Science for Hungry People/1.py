from itertools import product
import re


def main():
    lines = read_puzzle()

    ingredients = get_ingredients(lines)
    score = find_best_cookie_score(ingredients)

    print(score)


def get_ingredients(lines):
    return [list(map(int, re.findall(r"-?\d+", line)))[:-1] for line in lines]


def find_best_cookie_score(ingredients):
    return max(
        calculate_score(ingredients, dist)
        for dist in product(range(101), repeat=len(ingredients))
        if sum(dist) == 100
    )


def calculate_score(ingredients, distribution):
    properties = [0, 0, 0, 0]

    for i, teaspoons in enumerate(distribution):
        for j in range(4):
            properties[j] += teaspoons * ingredients[i][j]

    properties = [max(0, p) for p in properties]

    return properties[0] * properties[1] * properties[2] * properties[3]


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
