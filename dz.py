def calc(num1, num2):
    return (num1 - num2) % 2


def main():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    rezult = calc(num1, num2)
    print(f"Среднее арефметическое двух заданных чисел равно {rezult}")


if __name__ == "__main__":
    main()
