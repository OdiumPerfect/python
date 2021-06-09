import itertools


# Задание 1

def odd_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


odd_to_15 = odd_generator(15)

print(*odd_to_15)

# Задание 2

max_not_yield = 15
not_yield = (x for x in range(1, max_not_yield + 1, 2))

print(*not_yield)

# Задание 3

tutors = [
    'Иван',
    'Анастасия',
    'Петр',
    'Сергей',
    'Дмитрий',
    'Борис',
    'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tut_klass = (
    tuple((name, klass)) for name, klass in itertools.zip_longest(tutors, klasses)
)

for i in range(8):
    print(next(tut_klass))

# Задание 4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [el for i, el in enumerate(src) if i != 0 and el > src[i - 1]]

print(result)

# Задание 5

src_less5 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_less5 = [el for el in src_less5 if src_less5.count(el) == 1]
print(result_less5)
