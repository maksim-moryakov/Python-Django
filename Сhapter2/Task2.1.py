# Фукции для простейших матиматических действий

# Сложение
def sum(x, y):
    return x + y

# Вычитание
def subtraction(x, y):
    return x - y

# Умножение
def multiplication(x, y):
    return x * y

# Деление
def division(x, y):
    result = float(x / y)
    return result

# Возведение в степень
def exponentiation(x, y):
    return x ** y


x = int(input('Ведите число Х: '))
y = int(input('Введите чило Y: '))
print(f'x + y = {sum(x, y)}')
print(f'x - y = {subtraction(x, y)}')
print(f'x * y = {multiplication(x, y)}')
print(f'x / y = {division(x, y)}')
print(f'x ** y = {exponentiation(x, y)}')
