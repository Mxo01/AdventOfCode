from itertools import product

def main():
    lines = read_puzzle()

    total_calibration_sum = 0
    
    for line in lines:
        splitted = line.split(":")
        test_case = int(splitted[0])
        numbers = list(map(int, splitted[1].split(" ")[1:]))
        operators_combinations = list(product(["+", "*"], repeat=len(numbers) - 1))

        for i in range(len(operators_combinations)):
            result = numbers[0]
            
            for j in range(len(operators_combinations[i])):
                result = result + numbers[j + 1] if operators_combinations[i][j] == "+" else result * numbers[j + 1]
            
            if result == test_case:
                total_calibration_sum += test_case
                break

    print(total_calibration_sum)

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines

if __name__ == '__main__':
	main()
