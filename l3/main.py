# мультипарадигмальні мови прогр  , Разієвський Ілля
import math as m


print('мультипарадигм мови прогр , лаб 3 ')
print('Разієвський Ілля')

while True:
    try:
        x = float(input('Enter x value '))
        y = float(input('Enter y value '))
    except ValueError:
        print("Please enter a valid value")
        continue
    else:
        if (x >= 0):
            print(1 / (pow(x, 3) - pow(y, 3)) - m.sqrt(2 * x))
            break
        else:
            print('value under sqrt cant be negative , please enter valid x value  ')
            continue
