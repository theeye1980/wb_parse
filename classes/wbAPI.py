import json
import os
import subprocess
import requests

class wbAPI:
    #Разбор и обработка данных из файла клиента
    #На входе url, далее сохраняем при инициализации класса, парсим и работаем с тем, что есть
    def __init__(self, config):
        self.TOKEN_WB = config['TOKEN_WB']
        self.header = {
            'accept': 'application/json',
            'Authorization': self.TOKEN_WB,
            'Content-Type': 'application/json'
        }
        self.URL_WB_LIST = config['URL_WB_LIST']
        self.URL_WB_REVIEW_ARCHIVE_LIST = config['URL_WB_REVIEW_ARCHIVE_LIST']

    def get_wb_goods(self, limit):
        payload = {
            'sort': {
                'cursor': {
                    'limit': limit
                },
                'filter': {
                    'withPhoto': -1
                }
            }
        }

        response = requests.post(self.URL_WB_LIST, headers=self.header, json=payload)
        return response.json()

    def get_wb_reviews (self, nmId, limit):
        params = {
            'nmId': nmId,
            'take': limit,
            'skip': '0'
        }

        response = requests.get(self.URL_WB_REVIEW_ARCHIVE_LIST, headers=self.header, params=params)
        if response.status_code == 200:
            data = response.json()
            return response.json()

        else:
            print(f"Request failed with status code {response.status_code}")
        return response.json()