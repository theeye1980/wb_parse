import requests
import os
from dotenv import load_dotenv
from classes.db_my import DataMysql

load_dotenv()

config = {
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASS": os.getenv("DB_PASS"),
    "DB_NAME": os.getenv("DB_NAME"),
    "TOKEN_WB": os.getenv("TOKEN_WB"),
    "URL_WB_LIST": os.getenv("URL_WB_LIST"),

}



def get_wb_goods(limit):
    headers = {
        'accept': 'application/json',
        'Authorization': config['TOKEN_WB'],
        'Content-Type': 'application/json'
    }
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

    response = requests.post(config['URL_WB_LIST'], headers=headers, json=payload)
    return response.json()

# Example usage
response = get_wb_goods(600)
print(response)

# Пробегаемся по всем товарам и обновляем таблицу ID от ВБ и соответствие им артикулов

for item in response['data']['cards']:
    print(f"{item['nmID']} - {item['vendorCode']}")

data = []

for item in response['data']['cards']:
    imgs=[]
    nmID = item['nmID']
    vendorCode = item['vendorCode']
    brand = item['brand']
    data.append((nmID, vendorCode, brand))
    #Собираем массив фотографий для загрузки
    for img in item['mediaFiles']:
        imgURL=img
        imgs.append((nmID, imgURL))
    db.insert_wb_imgs_batch(imgs)
# Обновить информацию по связке ID на вб и артикул
#db.insert_wb_articles_batch(data)

