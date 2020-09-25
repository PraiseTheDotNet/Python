import re

if __name__ == '__main__':
    input = 'Ехал грека через реку ,видит грека— в реке рак .Сунул грека( рр )руку в реку :рак за руку греку — цап   !  цап цап цап.   .  .'
    words = sorted(list(set(re.findall(r'\w+', input))), key=str.lower)
    print(words)