import json


def main():
    lines = "".join(read_puzzle())

    sum = 0
    json_obj = json.loads(lines)

    for obj in json_obj:
        if type(obj) == int:
            sum += int(obj)
        elif type(obj) == dict:
            sum += process_dict(obj)
        elif type(obj) == list:
            sum += process_array(obj)

    print(sum)


def process_array(arr):
    if type(arr) == int:
        return arr

    sum = 0
    
    for obj in arr:
        if type(obj) == int:
            sum += int(obj)
        elif type(obj) == dict:
            sum += process_dict(obj)
        elif type(obj) == list:
            sum += process_array(obj)

    return sum


def process_dict(obj):
    if type(obj) == int:
        return obj

    sum = 0
    
    for key in obj:
        if type(obj[key]) == int:
            sum += int(obj[key])
        elif type(obj[key]) == dict:
            sum += process_dict(obj[key])
        elif type(obj[key]) == list:
            sum += process_array(obj[key])

    return sum


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()