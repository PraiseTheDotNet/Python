import re
from datetime import date


def format_with_regex(input: str):
    return re.sub(r'(?P<yy>\d{4})-(?P<mm>\d{1,2})-(?P<dd>\d{1,2})', r'\g<dd>/\g<mm>/\g<yy>', input)


def format_without_regex(input: str):
    return '/'.join(reversed(input.split('-')))

if __name__ == '__main__':
    # Получаем текущую дату
    d1 = date.today()
    # Преобразуем результат в строку
    ds = str(d1)
    input = str(d1)
    print('С регексом:')
    print(format_with_regex(input))
    print('Без регекса:')
    print(format_without_regex(input))