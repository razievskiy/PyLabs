num = int(input('Enter num : '))

count = 0

while num:
    num //= 10
    count += 1

print(count)