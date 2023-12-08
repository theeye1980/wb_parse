#получает отзывы по всем товарам
#Выгружает фото отзывов в папку wb_img_review
import os
from dotenv import load_dotenv
from classes.db_my import DataMysql
from classes.wbAPI import wbAPI
from classes.fileManager import fileManager

archive_review_depth = 35 #Количество отзывов к товару, которое просматривать. Если у вас много отзывов, можно увеличить
output_folder = 'wb_reviews' #Путь к выходной папке - можно заменить на свою
brand = 'ARTE LAMP' #Бренд, по которому вы хотите выдернуть фотографии в отзывах товаров

load_dotenv()

config = {
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASS": os.getenv("DB_PASS"),
    "DB_NAME": os.getenv("DB_NAME"),
    "TOKEN_WB": os.getenv("TOKEN_WB"),
    "URL_WB_LIST": os.getenv("URL_WB_LIST"),
    "URL_WB_REVIEW_ARCHIVE_LIST": os.getenv("URL_WB_REVIEW_ARCHIVE_LIST")}

# получим все товары из ВБ
wbAPI = wbAPI(config)
db=DataMysql(config)
wb_goods = db.get_wb_goods(brand)

# Пробежимся по всем товарам и посмотрим, нет ли за последний год там отзывов

for good in wb_goods:

    #Выдернем Архивные отзывы
    result = wbAPI.get_wb_reviews(good[0],archive_review_depth)
    try:
        num_feedbacks = len(result['data']['feedbacks'])
        if(num_feedbacks>0):

            #Пробегаем по всем отзывам
            for feedback in result['data']['feedbacks']:
                    print(feedback['id'])
                    print(feedback['text'])
                    print(feedback['productValuation'])
                    print(feedback['createdDate'])
                    print(feedback['productDetails']['nmId'])
                    print(feedback['productDetails']['supplierArticle'])

                    if feedback['photoLinks'] is not None:
                        num_photoLinks = len(feedback['photoLinks'])
                        if num_photoLinks > 0:
                            imgs = []
                            for photo_url in feedback['photoLinks']:
                                # Iterate through the photo links and display them
                                print(photo_url['fullSize'])
                                imgs.append(photo_url['fullSize'])
                            file_name = str(feedback['productDetails']['supplierArticle'] + "_" + feedback['id'])
                            fileManager.download_files(imgs, output_folder, file_name)
    except Exception as e:
                print("An error occurred:", str(e))




