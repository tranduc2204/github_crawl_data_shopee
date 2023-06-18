# Đề bài Yêu cầu: Quay video quá trình thực hiện cào giá trên shopee shop theo đường link bên dưới và lưu dữ liệu giá của mỗi sản phẩm dưới dạng timeseries
#Link shop: https://shopee.vn/unilever_vietnam

import requests
import json
import schedule
import time
from datetime import datetime
import pandas as pd
import os
import csv

# url = "https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset=60&shop_id=26947756&sort_type=1&upstream="
# url = "https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset=30&shop_id=26947756&sort_type=1&upstream="

# lưu header từng cột
filename = "c1_crawl_data.csv"
header = not os.path.exists(filename) 
with open (filename, encoding= "utf8", mode= "w", newline= "") as file_csv:
    header = ["timestamp", "name", "price", "price_min", "price_max", "price_min_before_discount", "price_max_before_discount", "itemid"]
    writer = csv.writer(file_csv)
    writer.writerow(header)

#
def function():
    df = pd.DataFrame(columns=["timestamp", "name", "price", "price_min", "price_max", "price_min_before_discount", "price_max_before_discount", "itemid"])
    x = 0
    for i in range (3):
        
        url = "https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset="+str(x)+"&shop_id=26947756&sort_type=1&upstream="
        x += 30 ## để lấy cả 3 trang
        
        headers = {
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43"
        }

        response = requests.get (url=url, headers= headers)
        json_dict = response.json()

        items_array = json_dict["data"]["items"]

        # filter các values cần lấy
        def filter_function(pair):
            key, value = pair
            return (key =="itemid") or (key == "name") or (key == "price") or (key == "price_min") or (key =="price_max") or (key == "price_min_before_discount") or (key == "price_max_before_discount")
        
        
        time_now = datetime.now()
        now_time_format = time_now.strftime("%Y-%m-%d %H:%M:%S")
        
        for i in range(len(items_array)):
            each = dict(filter(filter_function, items_array[i].items()))
            each["timestamp"] = now_time_format
            df = df.append(each, ignore_index=True)
        
        # lưu vào file
        df.to_csv(filename, mode = "a", index = False, header= False)
        # xóa hết trong dataframe để crawl trang sau không bị trùng data của trang trước
        df = df.drop(df.index).reindex(columns=["timestamp", "name", "price", "price_min", "price_max", "price_min_before_discount", "price_max_before_discount", "itemid"])
        
while True:
    function()
    time.sleep(600)# 1p sẽ có 60s --> 10p là 600s

