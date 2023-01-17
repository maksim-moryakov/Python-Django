# Массивы

array = [10, 11, 12, 13, 'Text', 14, 'Привет!', 'Мир']

# Длина массива
x = len(array)
print(x)
print('-' * 30)

# Берем элемент массива
print(array[4])
print('-' * 30)

# Элемент массива c отрицательным индексом
print(f'{array[-1]} {array[-2]}')
print('-' * 30)

# Цикл for по перебору массива
for i in array:
    print(i)

