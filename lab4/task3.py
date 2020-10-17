
def revert_dictionary(dict_items):
    list = [(value , key) for key, value in dict_items]
    res = {}
    for (k, v) in list:
        if k in res:
            res[k].append(v)
        else:
            res[k] = [v]
    return res



if __name__ == '__main__':
    some_dictionary = {1: 'dict', 2: 'dictionary', 3: 'dict'}
    print(some_dictionary)
    print(revert_dictionary(some_dictionary.items()))