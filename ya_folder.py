import requests
from pass_ya import token as TOKEN


URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

path_save = '2345'

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)

def check_folder(path_check):
    check_code = requests.get(f'{URL}?path={path_check}', headers=headers).status_code
    check = requests.get(f'{URL}?path={path_check}', headers=headers).json()
    if check_code == 200 and check['name'] == path_check:
        print(f'Папка  {path_check} присутствует в списке файлов.')
        return True
    else:print(f'Папки {path_check} НЕТ в списке файлов.') 
    return False

# Создаем папку
create_folder(path_save)   

# Проверяем наличие созданной папки          
assert check_folder(path_save) == True
assert check_folder('1122335666') == False