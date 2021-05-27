# Задание 1


duration = int(input('Введите значение в секундах: '))
hour = duration // 3600
minute = duration // 60 if (duration < 3600) else (duration // 60) % 60
second = duration % 60
# print(hour, minute, second)

if duration < 60:
    print(f'{second} сек')
elif (duration >= 60) and (duration < 3600):
    print(f'{minute} мин {second} сек')
elif (duration >= 3600) and (duration < 86400):
    print(f'{hour} час {minute} мин {second} сек')


# Задание 2
num_list = []
# Создаю список кубов нечетных числет от 1 до 1000
for i in range(1, 1000, 2):
    num_list.append(i ** 3)
print(num_list)
# a.

# Отбираю те, сумма которых кратна 7
sum_list_of_seven = []
for el in num_list:
    list_el = list(str(el))
    #    print(list_el)
    a = 0
    for i in list_el:
        a += int(i)
    #    print(a)
    if a % 7 == 0:
        sum_list_of_seven.append(el)
print(sum_list_of_seven)

# b.

# Делаю список с прибавлением 17
sum_list_of_seven_two = []
for el in num_list:
    el = el + 17
    sum_list_of_seven_two.append(el)

# Отбираю те, сумма которых кратна 7
sum_list_of_seven_three = []
for el in sum_list_of_seven_two:
    list_el = list(str(el))
    a = 0
    for i in list_el:
        a += int(i)
    if a % 7 == 0:
        sum_list_of_seven_three.append(el)
# print(sum_list_of_seven_two)
print(sum_list_of_seven_three)

# Задание 3
while True:
    user_percent = input('Введите число в процентах от 1 до 20: ')
    if int(user_percent) >= 1 and int(user_percent) <= 20:
        break
    else:
        print('Вы ввели неверное значение, попробуйте еще')
# "процента"
percent = {
    '1': 'процент',
    '2': 'процента',
    '3': 'процента',
    '4': 'процента',
    '5': 'процентов',
    '6': 'процентов',
    '7': 'процентов',
    '8': 'процентов',
    '9': 'процентов',
    '10': 'процентов',
    '11': 'процентов',
    '12': 'процентов',
    '13': 'процентов',
    '14': 'процентов',
    '15': 'процентов',
    '16': 'процентов',
    '17': 'процентов',
    '18': 'процентов',
    '19': 'процентов',
    '20': 'процентов',
}

print(f'Вы ввели {user_percent} {percent[user_percent]}')