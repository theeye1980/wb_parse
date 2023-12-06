#Загружаем wb картинки в папочку по списку url


import os

from dotenv import load_dotenv
from classes.db_my import DataMysql
from classes.fileManager import fileManager



load_dotenv()

config = {
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASS": os.getenv("DB_PASS"),
    "DB_NAME": os.getenv("DB_NAME"),
    "TOKEN_WB": os.getenv("TOKEN_WB"),
    "URL_WB_LIST": os.getenv("URL_WB_LIST"),

}
db=DataMysql(config)

#Сделаем выборку товаров консолей

db=DataMysql(config)
wb_goods = db.get_wb_goods('AllConsoles')

#Пробежимся по всем товарам и загрузим картинки в папочку

for good in wb_goods:
    print(good)
    #Выдернем все URL картинки для этого товара
    imgs = db.get_wb_img_by_wbid(good[0])
    print(imgs)
    #Сохраним все картинки в нормальном виде
    fileManager.download_files(imgs, 'wbimg', good[1])
print(wb_goods)


