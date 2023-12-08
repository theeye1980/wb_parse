import os
import urllib.request
import ssl
class fileManager:

    def __init__(self):
        print("Инициализируем")

    @staticmethod
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

                # Disable SSL certificate verification
                ssl._create_default_https_context = ssl._create_unverified_context
                urllib.request.urlretrieve(url, file_path)
                print(f"Downloaded: {filename1}")
                counter = counter + 1
        else:
            print("URL list is empty.")