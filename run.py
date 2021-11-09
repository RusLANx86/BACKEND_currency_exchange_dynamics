from pprint import pprint
from api import get_dict_of_currencies, get_currency_course_dynamics, save_to_file

print("Выберите действие:")
print("1 - Вывести все валюты и их 'VAL_NM_RQ")
print("2 - Вывести динамику курса валюты")
print("3 - Сохранить в файл")
print("Другая клавиша - Выход")
command = input()
curries = (get_dict_of_currencies(url="https://cbr.ru/currency_base/dynamics/"))
to_save = None
rates_of_cur = ""
while (command != "1" or command != "2" or command != "3"):
    if command == "1":
        to_save = keys = curries.keys()
        pprint(list(keys))
    elif command == "2":
        print("Укажите валюту")
        cur_name = str(input())
        rates_of_cur = curries[cur_name]
        to_save = currency_course_dynamics = get_currency_course_dynamics(VAL_NM_RQ=rates_of_cur)
        pprint(currency_course_dynamics)
    elif command == "3":
        if to_save != None:
            save_to_file(data=to_save)
        print("Сохранено")
    print()
    print("Выберите действие:")
    command = input()

print("Выход")