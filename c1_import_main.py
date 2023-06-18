import pandas as pd
import csv
from pymongo import MongoClient


# đọc file csv sau khi chạy main_c1.py
df = pd.read_csv("c1_crawl_data.csv")

# sắp xếp file để trình bày theo timeseries
df_sort = df.sort_values(by = ["itemid","timestamp"], ascending= True)

# tạo một bản sao lưu vào file csv
df_sort.to_csv("c1_file_kq_crawl.csv", index= False)

###################### Bước import vào db mongo
# Tạo kết nối tới MongoDB
client = MongoClient('mongodb://localhost:27017/')

# tạo và chọn db
db_name = 'db_crawl_data'
db = client[db_name]
db = client[db_name]

# tạo và chọn collection
collection_name = 'crawl'
collection = db[collection_name]
collection = db[collection_name]

# chuyển DataFrame thành danh sách các bản ghi (documents)
documents = df_sort.to_dict(orient='records')

# 1 bản lưu vào mongo
collection.insert_many(documents)

# xóa 
# collection.drop()
