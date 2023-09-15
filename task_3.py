'''
Напишите функцию принимающую на вход только ключевые параметры и
 возвращающую словарь, где ключ — значение переданного аргумента, 
 а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''

def create_dict_from_kwargs(**kwargs):
    result = {}
    for key, value in kwargs.items():
        key_str = str(value) if isinstance(value, (int, float, str, bool, tuple, frozenset)) else repr(value)
        result[key_str] = key
    return result

result_dict = create_dict_from_kwargs(a=1, b='hello', c=[1, 3, 5])
print(result_dict)

