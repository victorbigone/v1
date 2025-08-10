def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def main():
    try:
        n = int(input("Введите количество чисел Фибоначчи: "))
        if n <= 0:
            print("Введите положительное число!")
        else:
            print(f"Первые {n} чисел Фибоначчи: {fibonacci(n)}")
    except ValueError:
        print("Введите корректное число!")

if __name__ == "__main__":
    main()