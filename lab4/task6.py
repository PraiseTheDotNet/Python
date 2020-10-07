from os.path import join

def parse_list(data: list) -> dict:
    res = {}
    for el in data:
        text = el.split('-')
        name = text[0]
        price = int(text[1])
        res[name] = price
    return res

if __name__ == '__main__':
    dir = 'files/task6'
    f1 = open(join(dir, 'shop1.txt'), 'r', encoding="utf-8")
    first_shop = f1.read().splitlines()
    f1.close()
    f2 = open(join(dir, 'shop2.txt'), 'r', encoding="utf-8")
    second_shop = f2.read().splitlines()
    f2.close()
    res = parse_list(first_shop)
    l2 = parse_list(second_shop)
    for key in l2.keys():
        if key in res:
            res[key] = max(res[key], l2[key])
        else:
            res[key] = l2[key]
    f3 = open(join(dir, 'shop_max.txt'), 'w', encoding="utf-8")
    data = list(res.items())
    data = [key + '- ' + str(value) + '\n' for (key, value) in data]
    f3.writelines(data)
    f3.close()
