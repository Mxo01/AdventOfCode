import hashlib


def main():
    lines = read_puzzle()

    secret_key = lines[0].encode()
    i = 0

    while True:
        hash_secret = secret_key + str(i).encode()
        hash_md5 = hashlib.md5(hash_secret).hexdigest()

        if hash_md5[:5] == "00000":
            print(i)
            break

        i += 1


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
