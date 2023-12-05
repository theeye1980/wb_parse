import time
import json
import mysql.connector
from mysql.connector import Error
from os.path import isfile

class DataMysql:
    def __init__(self,config):

        self.db_connection = mysql.connector.connect(

            host=config['DB_HOST'],
            user=config['DB_USER'],
            passwd=config['DB_PASS'],
            database=config['DB_NAME']
        )
        self.db_cursor = self.db_connection.cursor()

### SELECT методы

    def get_wb_goods(self, brand):

        query = "SELECT nmID,wbVendorCode FROM wb_content WHERE brand = '%s'"
        # Fetch the result
        values = (brand)
        result_sql = query % values
        self.db_cursor.execute(result_sql)
        result = self.db_cursor.fetchall()

        # Return the category ID if found, otherwise return None
        if result:
            return result
        else:
            return None

    def get_wb_img_by_wbid(self, wbid):
        query = "SELECT imgURL FROM wb_imgs WHERE wbID = '%s'"
        # Fetch the result
        values = (wbid)
        result_sql = query % values
        self.db_cursor.execute(result_sql)
        result = self.db_cursor.fetchall()

        # Return the category ID if found, otherwise return None
        if result:
            imgURLs = [row[0] for row in result]
            return imgURLs

        else:
            return None
    def select_all_articles(self,projID):
        query = "SELECT id,article FROM articles where projectid = '%s'"
        values = (projID)
        result_sql = query % values
        self.db_cursor.execute(result_sql)
        result = self.db_cursor.fetchall()
        if result:
            # Define a dictionary to store the id by category
            return result
        else:
            return None

### Insert методы
        # query = "INSERT INTO articles (article, imgpath, goodpath) VALUES (%s, %s, %s)"
        # data = (article, imgpath, goodpath)
    def insert_wb_articles_batch(self, data):
        try:
            self.db_cursor.executemany(
                "INSERT INTO wb_content (nmID, wbVendorCode,brand) VALUES (%s, %s, %s)", data)
            self.db_connection.commit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    def insert_wb_imgs_batch(self, data):
        try:
            self.db_cursor.executemany(
                "INSERT INTO wb_imgs (wbID, imgURL) VALUES (%s, %s)", data)
            self.db_connection.commit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    def insert_categories(self, category, projID,xmlid):
        query = "INSERT INTO categories (category, projectid,xmlid) VALUES ('%s', %s, %s)"
        update_data = (category, projID, xmlid)
        result_sql = query % update_data
        print(result_sql)

        try:
            self.db_cursor.execute(result_sql)
            self.db_connection.commit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    ### UPDATE

    def mark_art_true(self, id):
        update_query = "UPDATE articles SET status = True WHERE id = %s"
        update_data = (id)
        result_sql = update_query % update_data
        print(result_sql)
        try:
            # time.sleep(1)
            self.db_cursor.execute(result_sql)
            # time.sleep(1)
            self.db_connection.commit()
        except mysql.connector.Error as error:
            print("Failed to update table record: {}".format(error))



    def close(self):
        self.db_cursor.close()
        self.db_connection.close()