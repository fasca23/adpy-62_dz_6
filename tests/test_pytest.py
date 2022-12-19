import pytest
from parameterized import parameterized
from home_work_4_1 import sample_country
from home_work_4_2 import unique_ids
from home_work_4_5 import cutting
from ya_folder import create_folder, URL, headers, delete_folder
import time
import requests


FIXTURE = [
    ('Москва', [{'visit1': ['Москва', 'Россия']}]),
    ('Тула', [{'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}]),
    ('Москва', [{'visit1': ['Москва', 'Россия']}])
]

@parameterized.expand(FIXTURE)
def test_home_work_4_1(a, b):
    result = sample_country(a)
    etalon = b
    assert result == etalon

def test_home_work_4_2():
    result = unique_ids()
    etalon = {98, 35, 15, 213, 54, 119}
    assert result == etalon
    
def test_home_work_4_5():
    result = cutting()
    etalon = {'2018-01-01': {'yandex': {'cpc': {100: 123}}}}
    assert result == etalon
        
def test_check_folder(path_check = "1234"):
    create_folder(path_check)
    check_code = requests.get(f'{URL}?path={path_check}', headers=headers).status_code
    check = requests.get(f'{URL}?path={path_check}', headers=headers).json()
    if check_code == 200 and check['name'] == path_check:
        result = True
    else:result = False
    time.sleep(5)
    delete_folder(path_check)
    assert result == True