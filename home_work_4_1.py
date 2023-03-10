
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def input_country():
     while True:
         country = input(f'\n Визиты из какой страны/города оставить : ')
         if country.isalpha() and country: 
             return country.capitalize()
# country = input_country()

def sample_country(country_):
  return [
    log for log in geo_logs 
    if country_ in next(iter(log.values()))]
