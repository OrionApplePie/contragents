import requests
from bs4 import BeautifulSoup
import json
import os
from random import choice
from time import sleep
from random import uniform


def get_html(url, useragent=None, proxy=None):
    print('get html ...')
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text


def get_ip(html):
    print('proxy and user agent')
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip)
    print(ua)
    print('-------------------------')


def get_contragents_list(search_string='', page_number=1):
    """
    Функция для получения списка контрагентов по ключевому слову

    :param search_string:
    :return:
    """
    url = 'https://sbis.ru/sbisru/service/sbis-rpc-service300.dll'
    payload = '''
        {
          "jsonrpc":"2.0",
          "protocol":4,
          "method":"Контрагент.List",
          "params":{
                      "Фильтр":{
                                "s":[{"n":"Реквизиты","t":"Строка"},
                                     {"n":"Состояние","t":"Строка"}],
                                "d":["",null],
                                "_type":"record"
                                },
                      "Сортировка":{
                                "s":[{"n":"l","t":"Логическое"},
                                     {"n":"n","t":"Строка"},
                                     {"n":"o","t":"Логическое"}],
                                "d":[[false,"Выручка",true]],
                                "_type":"recordset"
                                },
                      "Навигация":{
                                   "s":[{"n":"ЕстьЕще","t":"Логическое"},
                                        {"n":"РазмерСтраницы", "t":"Число целое"},
                                        {"n":"Страница","t":"Число целое"}],
                                   "d":[true,30,0],
                                   "_type":"record"
                                   },
                      "ДопПоля":[]
                    },
          "id":1
        }
    '''
    module_dir = os.path.dirname(__file__)
    useragents_path = os.path.join(module_dir, 'useragents.txt')
    proxies_path = os.path.join(module_dir, 'proxies')

    useragents = open(useragents_path).read().split('\n')
    proxies = open(proxies_path).read().split('\n')
    useragent = {'User-Agent': choice(useragents)}
    proxy = {'http': 'https://' + choice(proxies)}

    data = json.loads(payload)
    data['params']["Фильтр"]["d"][0] = search_string
    data['params']["Навигация"]["d"][2] = page_number

    response = requests.post(url, json=data, headers=useragent, proxies=proxy)
    res = response.json()
    return res
