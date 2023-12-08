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

    def get_all_wb_cards(self):
        limit = 1000
        with_photo = -1
        cards = []

        # Первый запрос
        response = self.make_request(limit, with_photo)
        data = response['data']
        cards.extend(data['cards'])
        cursor = data['cursor']

        # Повторяем запросы, пока не получим все карточки
        while cursor['total'] >= limit:
            cursor_query = {
                "updatedAt": cursor["updatedAt"],
                "nmID": cursor["nmID"]
            }

            print(cursor_query)
            response = self.make_request(limit, with_photo, cursor_query)
            data = response['data']
            cards.extend(data['cards'])
            cursor = data['cursor']

        return cards

    def make_request(self, limit, with_photo, cursor_query=None):
        payload = {
            'sort': {
                'cursor': {
                    'limit': limit
                },
                'filter': {
                    'withPhoto': with_photo
                }
            }
        }

        if cursor_query:
            payload = {
                'sort': {
                    'cursor': {
                        'limit': limit,
                        'updatedAt': cursor_query['updatedAt'],
                        'nmID': cursor_query['nmID']
                    },
                    'filter': {
                        'withPhoto': with_photo
                    }
                }
            }

        response = requests.post(self.URL_WB_LIST, json=payload, headers=self.header)
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