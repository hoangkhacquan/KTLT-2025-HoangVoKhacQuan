print("Sinh vien: Hoang Vo Khac Quan")
print("Ma so sv: 245752021610150")
s = input("Nhập chuỗi: ")
chuoi_moi = ""
for ch in s:
    if not ch.isdigit():
        chuoi_moi += ch
print("Chuỗi sau khi bỏ chữ số:", chuoi_moi)
