import io
import json


def read_menu_element(max: int) -> int:
    res: int = max
    while res >= max:
        print('Введите номер пункта:', end='\n')
        res = read_int()
    return res


def read_string(title=None) -> str:
    res = ''
    while not len(res):
        if title:
            print(title)
        res = input()
    return res


def read_int(title=None) -> int:
    res: int
    while True:
        if title:
            print(title, end='\n')
        text = input()
        if text.isdigit():
            res = int(text)
            break
    return res


def print_menu(elements: list, title: str=None) -> int:
    if title:
        print(title, end='\n')
    for i in range(len(elements)):
        print(i, elements[i])
    item = read_menu_element(len(elements))
    print('Выбран пункт меню:', elements[item])
    return item


def print_country_info(data: dict, country: str):
    print('Страна:', country, end='\n')
    for (key, value) in data[country].items():
        print('\tТовар:', key + ', вес:', value, 'т.')


def get_products(data: dict) -> dict:
    products = {}
    for country in data.keys():
        for (county_product, weight) in data[country].items():
            if county_product not in products:
                products[county_product] = [(country, weight)]
            else:
                products[county_product].append((country, weight))
    return products


if __name__ == '__main__':
    main_menu = ['Добавить данные в файл', 'Вывести всю информацию', 'Вывести список товаров заданной страны',
                 'Вывести список стран, эскпортирующих заданный товар', 'Выход']

    f = io.open('files/task7/input.txt', 'r', encoding='utf-8')
    data = json.load(f)
    f.close()
    while True:
        print(end='\n')
        elem = print_menu(main_menu, 'Главное меню')
        if elem == 0:
            select_country_menu = list(data.keys())
            select_country_menu.append('Новая страна')
            select_country_menu.append('Главное меню')
            country = print_menu(select_country_menu, 'Выберите страну')
            country_name: str
            if country == len(select_country_menu) - 1:
                continue
            elif country == len(select_country_menu) - 2:
                country_name = read_string('Введите название страны')
                data[country_name] = {}
            else:
                country_name = select_country_menu[country]

            products = get_products(data)
            select_product_menu = list(products.keys())
            select_product_menu.append('Добавить новый товар')
            select_product_menu.append('Главное меню')
            product_id = print_menu(select_product_menu, 'Выберите товар')

            product_name: str

            if product_id == len(select_product_menu) - 1:
                continue
            elif product_id == len(select_product_menu) - 2:
                product_name = read_string('Введите название товара')
            else:
                product_name = select_product_menu[product_id]

            if product_name in data[country_name]:
                print('Текущее количество составляет: ', data[country_name][product_name], 'т.', end='\n')
            count = read_int('Введите количество экспортируемого товара в тоннах')

            data[country_name][product_name] = count
            with io.open('files/task7/input.txt', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        elif elem == 1:
            countries = list(data.keys())
            for country in countries:
                print_country_info(data, country)
        elif elem == 2:
            select_country_menu = list(data.keys())
            select_country_menu.append('Главное меню')
            country = print_menu(select_country_menu, 'Выберите страну')
            if country != len(select_country_menu):
                print_country_info(data, select_country_menu[country])
        elif elem == 3:
            products = get_products(data)
            select_product_menu = list(products.keys())
            select_product_menu.append('Главное меню')
            product_id = print_menu(select_product_menu, 'Выберите товар')
            if product_id != len(products):
                prod = select_product_menu[product_id]
                print('Экспортёры товара', prod + ':', end='\n')
                for (cntr, weight) in products[prod]:
                    print('\t' + cntr + ': ' + str(weight) + ' т.', end='\n')
        else:
            break
