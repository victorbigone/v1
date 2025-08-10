def filter_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]

def main():
    try:
        numbers = input("Введите числа через пробел: ").split()
        numbers = [int(num) for num in numbers]
        threshold = int(input("Введите пороговое значение: "))
        filtered = filter_numbers(numbers, threshold)
        print(f"Числа больше {threshold}: {filtered}")
    except ValueError:
        print("Ошибка: введите корректные числа!")

if __name__ == "__main__":
    main()