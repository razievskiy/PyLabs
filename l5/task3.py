def square_root(number, epsilon):
    x = number / 2  # початкове наближення - половина вхідного числа
    while abs(x**2 - number) > epsilon:
        x = (x + number / x) / 2  # формула Герона
    return x


number = float(input("Введіть число: "))
epsilon = 1e-4

result = square_root(number, epsilon)
print("Квадратний корінь числа", number, "дорівнює", result)