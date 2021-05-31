# Задание 1

print(15 * 3)
print(15 / 3)
print(15 // 2)
print(15 ** 2)

# Задание 2

lesson_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list = []
for i in lesson_list:
    if i.isdigit():
        my_list.extend(['"', i, '"'])
    elif ('+' or '-' in i) and len(i) == 2:
        i = list(i)
        i.insert(1, '0')
        i = ''.join(i)
        my_list.extend(['"', i, '"'])
    else:
        my_list.append(str(i))
print(my_list)
print(' '.join(my_list))

# Задание 4

list_task4 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
for i in list_task4:
    i = i.split(' ')
    name = i.pop()
    name = name.title()
    print(f'Привет, {name}!')

# Задание 5

# A)
my_list = [57.8, 46.51, 97, 14, 55, 34.5, 12.86, 77.77, 44, 55]
new_my_list = []

# перебираю элементы списка, отсеиваю дробные и привожу к формату 2 чисел после запятой
for i in my_list:
    if '.' in str(i):
        a = str(i).split('.')
        if len(a[1]) == 1:
            b = a.pop()
            d = f'0{b}'
            a.append(d)
            new_my_list.append(float('.'.join(a)))
        else:
            new_my_list.append(i)
    else:
        new_my_list.append(i)

print(new_my_list)

# вывод списка в формате ХХ рублей ХХ копеек
for i in my_list:
    if type(i) == float:
        a = str(i).split('.')
        print(f'{a[0]} рублей {a[1]} копеек')
    else:
        print(f'{i} рублей 00 копеек')

# B)
print(new_my_list)
print(id(new_my_list))
new_my_list.sort()
print(new_my_list)
print(id(new_my_list))

# C)

new_my_list.reverse()
print(new_my_list)

# D)
# тут уже применена сортировка, поэтому можно так. С другим листом с сортировкой и вывод по срезу
print(new_my_list[0:5])