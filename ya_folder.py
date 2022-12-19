import requests
from pass_ya import token as TOKEN


URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

path_save = '2345678910111213'

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)
    
def delete_folder(path):
    requests.delete(f'{URL}?path={path}', headers=headers)