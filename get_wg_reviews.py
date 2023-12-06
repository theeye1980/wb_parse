#получает отзывы по всем товарам
#Выгружает фото отзывов в папку wb_img_review
import os
from dotenv import load_dotenv
from classes.db_my import DataMysql
from classes.wbAPI import wbAPI
from classes.fileManager import fileManager



load_dotenv()

config = {
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASS": os.getenv("DB_PASS"),
    "DB_NAME": os.getenv("DB_NAME"),
    "TOKEN_WB": os.getenv("TOKEN_WB"),
    "URL_WB_LIST": os.getenv("URL_WB_LIST"),
    "URL_WB_REVIEW_ARCHIVE_LIST": os.getenv("URL_WB_REVIEW_ARCHIVE_LIST")}

# получим все товары Allconsoles из ВБ
wbAPI = wbAPI(config)
db=DataMysql(config)
wb_goods = db.get_wb_goods('AllConsoles')

# Пробежимся по всем товарам и посмотрим, нет ли за последний год там отзывов

for good in wb_goods:
    print(good)
    #Выдернем Архивные отзывы
    result = wbAPI.get_wb_reviews(good[0],25)
    num_feedbacks = len(result['data']['feedbacks'])
    if(num_feedbacks>0):
        # print(result)
        #Пробегаем по всем отзывам
        for feedback in result['data']['feedbacks']:
            print(feedback['id'])
            print(feedback['text'])
            print(feedback['productValuation'])
            print(feedback['createdDate'])
            print(feedback['productDetails']['nmId'])
            print(feedback['productDetails']['supplierArticle'])

            if(feedback['photoLinks'] != None):
                num_photoLinks = len(feedback['photoLinks'])
                if (num_photoLinks > 0):
                    imgs=[]
                    for photo_url in feedback['photoLinks']:
                        #Перебираем фоточки и показываем
                        print(photo_url['fullSize'])
                        imgs.append(photo_url['fullSize'])
                    file_name = str(feedback['productDetails']['supplierArticle'] + "_" + feedback['id'])
                    fileManager.download_files(imgs, 'wb_reviews', file_name)


    # if result['data']['feedbacks']['video'][0] != None:
    #     print("Ахтунг - видео есть")
    #     print(result['data']['feedbacks']['video'][0])



