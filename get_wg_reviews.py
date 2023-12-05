#получает отзывы по всем товарам
#Выгружает фото отзывов в папку wb_img_review

from dotenv import load_dotenv
from classes.db_my import DataMysql
import os

load_dotenv()

config = {
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASS": os.getenv("DB_PASS"),
    "DB_NAME": os.getenv("DB_NAME"),
    "TOKEN_WB": os.getenv("TOKEN_WB"),
    "URL_WB_LIST": os.getenv("URL_WB_LIST")}

# получим все товары Allconsoles из ВБ

db=DataMysql(config)
wb_goods = db.get_wb_goods('AllConsoles')

# Пробежимся по всем товарам и посмотрим, нет ли за последний год там отзывов

for good in wb_goods:
    print(good)
    #Выдернем Архивные отзывы и обычные отзывы



