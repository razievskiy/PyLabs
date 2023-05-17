def check(value) :
    for i in range(2, (value//2) + 1):
        if value % i == 0:
            return False

    return True


val = int(input('Enter value :  '))

nextValue = val+1

count = 0

while count < 5:
    if check(nextValue):
        print(nextValue)
        count += 1
    nextValue += 1
