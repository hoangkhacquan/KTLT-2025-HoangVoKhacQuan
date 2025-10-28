print("Sinh vien: Hoang Vo Khac Quan")
print("Ma so sv: 245752021610150")
def benefit(P, n):
    rate = 0.04
    A = P * (1 + rate) ** n
    return A
P = float(input("Nhập số tiền ban đầu: "))
n = int(input("Nhập số năm gửi: "))
tien_nhan_duoc = benefit(P, n)
print("Số tiền nhận được sau", n, "năm là:", round(tien_nhan_duoc, 2))
