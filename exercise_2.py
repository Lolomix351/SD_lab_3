# Шакула Дмитрий Андреевич 090301-ПОВа-о24

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Считываем входные данные
a, b, c = map(int, input().split())

# Находим НОД(a, b)
d = gcd(a, b)

# Проверяем, делит ли НОД число c
if c % d == 0:
    print(d)
else:
    print("Impossible")


print("Выполнил Шакула Дмитрий Андреевич 090301-ПОВа-о24")