import mysql.connector

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

    def get_art_by_wbid(self, wbid):
            query = "SELECT wbVendorCode FROM wb_content WHERE nmID = '%s'"
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

### Insert методы

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


    def close(self):
        self.db_cursor.close()
        self.db_connection.close()