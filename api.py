import requests
from bs4 import BeautifulSoup as bs


def get_dict_of_currencies(url: str) -> dict:
      r = requests.get(url)
      soup = bs(r.text, "html.parser")
      currencies = soup.findAll("option")
      dict_of_currencies = {}
      for currency in currencies:
          key = currency.text.strip()
          val = currency.attrs["value"]
          dict_of_currencies[key] = val
      return dict_of_currencies

def get_currency_course_dynamics(VAL_NM_RQ, Posted=True, so=1, mode=1, From="28.10.2021", To="04.11.2021") -> list:
      url = "https://cbr.ru/currency_base/dynamics/" \
            "?UniDbQuery.Posted={Posted}" \
            "&UniDbQuery.so={so}" \
            "&UniDbQuery.mode={mode}" \
            "&UniDbQuery.VAL_NM_RQ={VAL_NM_RQ}" \
            "&UniDbQuery.From={From}" \
            "&UniDbQuery.To={To}".format(Posted=Posted,
                                               so=so,
                                               mode=mode,
                                               VAL_NM_RQ=VAL_NM_RQ,
                                               From=From,
                                               To=To
                                               )
      r = requests.get(url)
      soup = bs(r.text, "html.parser")
      currency_course_dynamics_html_table = soup.findAll("tr")

      currency_course_dynamics = []

      for currency_rate in currency_course_dynamics_html_table:
            c = currency_rate.text.split("\n")
            cc = list(filter(None, c))
            currency_course_dynamics.append(cc)

      return currency_course_dynamics


def save_to_file(data, file_name="currency_course_dynamics.txt") -> bool:
    try:
        with open(file_name, "w") as f:
            for currency_rate in data:
                st = str(currency_rate)
                f.write(st + "\n")
    except Exception as ex:
        print(ex.__traceback__)
        return False
    else:
        return True
