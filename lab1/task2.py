
if __name__ == "__main__":
    print('Введите x')
    x = float(input())
    print('Введите y')
    y = float(input())
    if x == 0 and y == 0:
        print('Лежит в начале координат')
    elif x == 0:
        print('Лежит на оси ординат')
    elif y == 0:
        print('Лежит на оси абсцисс')
    else:
        if y > 0:
            if x > 0:
                print('I четверть')
            else:
                print('II четверть')
        elif x < 0:
            print('III четверть')
        else:
            print('IV четверть')
