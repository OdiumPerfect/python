from random import randrange, shuffle

# Задание 1

vocabulary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
}


def num_translate(eng_word):
    print(vocabulary[eng_word])


num_translate('nine')


# Задание 3

def thesaurus(*name):
    thesaurus_dict = {}
    for el in name:
        letter = el[0]
        thesaurus_dict.setdefault(letter, [])
        thesaurus_dict[letter].append(el)
    print(thesaurus_dict)


thesaurus('Иван', 'Мария', 'Петр', 'Илья')

# Задание 5

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_joke(count):
    ''' Функция берет случайные слова из трех списков и соединяет их в count шуток. '''
    for i in range(count):
        idx_one = randrange(len(nouns))
        idx_two = randrange(len(adverbs))
        idx_three = randrange(len(adjectives))
        print(f'{nouns[idx_one]} {adverbs[idx_two]} {adjectives[idx_three]}')


get_joke(2)


def get_joke_v1(count, repeat):
    ''' Вторым аргументом: True - Включение режима защиты от повторов слов, False - режим неактивен'''
    if repeat is False:
        for i in range(count):
            idx_one = randrange(len(nouns))
            idx_two = randrange(len(adverbs))
            idx_three = randrange(len(adjectives))
            print(f'{nouns[idx_one]} {adverbs[idx_two]} {adjectives[idx_three]}')
    elif repeat is True:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for i in range(count):
            print(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')


get_joke_v1(3, True)
