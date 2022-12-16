a = ['2018-01-01', 'yandex', 'cpc', 100, 123]

def cutting(a):
    d = a[-1]
    for i in a[-2::-1]:
        d = {i: d}
    return d

assert cutting(a=a) == {'2018-01-01': {'yandex': {'cpc': {100: 123}}}}
