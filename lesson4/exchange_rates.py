import sys
import argparse
from requests import get, utils
from decimal import Decimal

# Задание 2
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


# print(content)


def currency_rates(currency):
    currency = currency.upper()
    my_split = content.split('<CharCode>')
    my_list = []
    for el in my_split:
        value = el[:3]
        my_list.append(value)
        if value == currency:
            filter_rates = el.split('<Value>')
            filter_rates = str(filter_rates[1])[:7]
            filter_rates = filter_rates.replace(',', '.')
            filter_rates = float(filter_rates)
            print(f'Курс {currency} = {filter_rates}')
        elif value != currency:
            pass

    if currency not in my_list:
        print(None)


if __name__ == '__main__':
    currency_rates('EUR')
    # Задание 5
    method_name = sys.argv[1]
    parameter_name = str(sys.argv[2])
    getattr(sys.modules[__name__], method_name)(parameter_name)

