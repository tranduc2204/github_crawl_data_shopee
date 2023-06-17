# Đề bài Yêu cầu: Quay video quá trình thực hiện cào giá trên shopee shop theo đường link bên dưới và lưu dữ liệu giá của mỗi sản phẩm dưới dạng timeseries
#Link shop: https://shopee.vn/unilever_vietnam

import requests
import json
import schedule
import time

# url = "https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset=60&shop_id=26947756&sort_type=1&upstream="
# url = "https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset=30&shop_id=26947756&sort_type=1&upstream="

def function():
    for i in range (3):
        x = 0
        url = "https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset="+str(x)+"&shop_id=26947756&sort_type=1&upstream="
        x += 30## để lấy cả 3 trang
        
        headers = {
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43"
        }

        response = requests.get (url=url, headers= headers)
        json_dict = response.json()

        items_array = json_dict["data"]["items"]
        # print (items_array)
        # lấy các key values cần thiết # chúng ta cần lấy tên và giá
        def filter_function(pair):
            key, value = pair
            return (key == "name") or (key == "price") or (key == "price_min") or (key =="price_max") or (key == "price_min_before_discount") or (key == "price_max_before_discount")

        result = []
        for i in range(len(items_array)):
            each =  dict (filter(filter_function, items_array[i].items()))
            result.append(each)
        # nội dung end
        result_json = json.dumps(result, ensure_ascii=False, indent=4)

        # ghi vào file 
        # em sẽ chuyển thành mode a vì sẽ phải chạy for nếu để w nó ssex không lưu được cả 3 
        with open("kq.txt", "a", encoding="utf8") as file:
            file.write(result_json)


# function()

# hoàn thành chức năng crawl sp về 

# em có hỏi chị HR thì chị bảo em sau 10p sẽ crawl giá về 1 lần

while True:
    function()
    time.sleep(600)# 1p sẽ có 60s --> 10p là 600s













