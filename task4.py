# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('введите число: '))
s = input('введите индексы через пробел --> ')
numbers = []
mult = 1
for el in range(-n, n+1):
    numbers.append(el)
    print(f'{el}', end = ', ')
print(' ')              # не пойму, почему без этого принта, и вывод списка, и вывод решения, в одну строку
for i in s:
    if i != ' ':
        mult *= numbers[int(i)]
print(f'произведение элементов на указанных индексах = {mult}')
