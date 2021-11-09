import requests
user_id = 12345
url = 'https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.VAL_NM_RQ=R01010&UniDbQuery.From=28.10.2021&UniDbQuery.To=04.11.2021'
r = requests.get(url)
with open('test.html', 'w') as output_file:
    output_file.write(r.text)
