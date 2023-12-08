# Скрипт позволяет спарсить текущие цены на товары, которые продаются у конкеретного поставщика на Wildberries

import requests
from datetime import datetime

URL = "https://catalog.wb.ru/sellers/catalog"
PAYLOAD = {
    "TestGroup": "no_test",
    "TestID": "no_test",
    "appType": 1,
    "curr": "rub",
    "dest": -1257786,
    "page": 1,
    "regions": [80, 38, 83, 4, 64, 33, 68, 70, 30, 40, 86, 75, 69, 1, 31, 66, 110, 48, 22, 71, 114],
    "sort": "popular",
    "spp": 32,
    "supplier": 928362 #ID поставщика, меняем на своего и выкачиваем все товары, которые на вб у него и текущие цены
}

def get_data_from_wb(url_wb, payload_wb):
    list_product = []
    while True:
        response = requests.get(url=url_wb, params=payload_wb)
        data = response.json()

        payload_wb["page"] += 1
        data_list = data.get("data").get("products")
        if data_list:
            for i in data_list:
                id_product = i.get("id")
                name = i.get("name")
                brand = i.get("brand")
                name = brand
                price_u = int(i.get("priceU")) / 100
                sale_price_u = int(i.get("salePriceU")) / 100
                new_data = {
                    "id_product": id_product,
                    "name": name,
                    "brand": brand,
                    "priceU": price_u,
                    "salePriceU": sale_price_u
                }
                list_product.append(new_data)
        else:
            payload_wb["page"] = 1
            break

    data_wb = {
        "current_datetime": datetime.now().isoformat(),
        "data": list_product
    }

    return data_wb

data_wb = get_data_from_wb(url_wb=URL, payload_wb=PAYLOAD)
print(data_wb)