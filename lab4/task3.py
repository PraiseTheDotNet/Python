
def revert_dictionary(dict_items):
    return {value:key for key, value in dict_items}


if __name__ == '__main__':
    some_dictionary = {1: 'dict', 2: 'dictionary'}
    print(some_dictionary)
    print(revert_dictionary(some_dictionary.items()))