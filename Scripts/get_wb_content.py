import requests
import os
from dotenv import load_dotenv
from classes.db_my import DataMysql
from classes.wbAPI import wbAPI

load_dotenv()

config = {
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASS": os.getenv("DB_PASS"),
    "DB_NAME": os.getenv("DB_NAME"),
    "TOKEN_WB": os.getenv("TOKEN_WB"),
    "URL_WB_LIST": os.getenv("URL_WB_LIST"),
    "URL_WB_REVIEW_ARCHIVE_LIST":os.getenv("URL_WB_REVIEW_ARCHIVE_LIST"),

}
db=DataMysql(config)
wbAPI = wbAPI(config)

response = wbAPI.get_all_wb_cards()

# Пробегаемся по всем товарам и обновляем таблицу ID от ВБ и соответствие им артикулов
for item in  response:
    print(f"{item['nmID']} - {item['vendorCode']}")

data = []

for item in response:
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

# Вставить информацию по связке ID на вб и артикул
db.insert_wb_articles_batch(data)

