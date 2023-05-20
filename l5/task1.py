import math as m


n = 1
eps = 0.0001
sum_row = 0
a = 1

while abs(a) > eps:
    a = n ** 3 / m.factorial(3 * n - 3)
    n += 1
    sum_row += a

print(round(sum_row, 4))