#Загружаем wb картинки в папочку по списку url

import requests
import os
import urllib.request
from dotenv import load_dotenv
from classes.db_my import DataMysql


def download_files(url_list, folder_path, name):
    counter = 0

    if url_list:
        for url in url_list:
            filename, extension = os.path.splitext(os.path.basename(url))
            filename1 = name + '_' + str(counter) + extension
            file_path = os.path.join(folder_path, filename1)

            if os.path.exists(file_path):
                print(f"File {file_path} already exists. Skipping...")
                continue

            urllib.request.urlretrieve(url, file_path)
            print(f"Downloaded: {filename1}")
            counter = counter + 1
    else:
        print("URL list is empty.")

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
    download_files(imgs, 'wbimg', good[1])
print(wb_goods)


