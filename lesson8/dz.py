import re
from functools import wraps

# Задание 1
EMAIL = re.compile('([a-zA-Z0-9]+)@([a-zA-Z0-9]+).([a-z]+)')


def email_parse(adress):
    email_split = EMAIL.split(adress)
    user_name = email_split[1]
    user_domain = email_split[2]
    task1_dict = {f'{user_name}': f'{user_domain}'}
    if adress == str(email_split[1] + '@' + email_split[2] + '.' + email_split[3]):
        return task1_dict
    else:
        raise ValueError('Некорректный формат адреса')


print(email_parse('ilyaharin88@mail.ru'))
# print(email_parse('some!!!!!!!!!one@geekbrains.ru'))


# Задание 3

def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for i in args:
            print(f'{func.__name__}({i}: {type(i)})')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    """ Документация по функции calc_cube """
    calc = []
    for i in args:
        calc.append(i ** 3)
    return calc


a = calc_cube(2, 4, 7)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)



