# github_crawl_data_shopee
# decription cách 1
cách 1: có 2 file python và 2 file csv
  c1_main.py: là file sẽ crawl dữ liệu của shopee về và lưu tất cả dữ liệu đã crawl vào file c1_crawl_data.csv.
  c1_import_main.py: là file sẽ trình bày các sản phẩm theo kiểu timeseries và sau đó lưu vào db mongo. đồng thời lưu 1 file backup vào file c1_file_kq.csv.

cách 2: cos 2 file python
  c2_main.py: là file sẽ crawl dữ liệu của shopee về và lưu trực tiếp vào db mongo/
  c2_file_select.py: là file sẽ truy xuất dữ liệu trực tiếp từ db mongo sau đó sắp xếp dữ liệu theo kiểu timeseries và in ra màn hình. 
