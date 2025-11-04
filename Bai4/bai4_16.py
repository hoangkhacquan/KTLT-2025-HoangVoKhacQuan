print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
chuoi = input("Nhập chuỗi các số, cách nhau bằng dấu phẩy: ")
ds_chuoi = chuoi.split(",")
ds_so = [int(x) for x in ds_chuoi]
print("Danh sách các số nguyên là:")
print(ds_so)
