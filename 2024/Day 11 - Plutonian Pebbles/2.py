def main():
    line = read_puzzle()[0]
    print(
        sum(
            get_stones_after_blink(stone, 75)
            for stone in [int(n) for n in line.split(" ")]
        )
    )


def get_stones_after_blink(stone, blinks, cache={}):
    if blinks == 0:
        return 1

    if blinks in cache and stone in cache[blinks]:
        return cache[blinks][stone]
    else:
        cache.setdefault(blinks, {})

    generated_stones = 0

    if stone == 0:
        generated_stones = get_stones_after_blink(1, blinks - 1, cache)
    elif is_even(stone):
        first_half, second_half = split_stone(stone)
        generated_stones = get_stones_after_blink(
            first_half, blinks - 1, cache
        ) + get_stones_after_blink(second_half, blinks - 1, cache)
    else:
        generated_stones = get_stones_after_blink(stone * 2024, blinks - 1, cache)

    cache[blinks][stone] = generated_stones

    return generated_stones


def split_stone(stone):
    return int(str(stone)[: len(str(stone)) // 2]), int(
        str(stone)[len(str(stone)) // 2 :]
    )


def is_even(stone_length):
    return len(str(stone_length)) % 2 == 0


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
