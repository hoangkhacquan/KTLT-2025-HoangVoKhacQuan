print("Sinh vien: Hoang Vo Khac Quan")
print("Ma so sv: 245752021610150")
S = input("Nhap chuoi")
kq=""
for ch in S:
    if ch.isalpha():
        kq+=ch.upper()
print("Ket qua:", kq)
