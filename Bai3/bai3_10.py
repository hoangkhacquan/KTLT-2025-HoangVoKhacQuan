print("Sinh vien: Hoang Vo Khac Quan")
print("Ma so sv: 245752021610150")
import math
def getCircle(R):
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    return (chu_vi, dien_tich)
R = float(input("Nhập bán kính hình tròn: "))
chu_vi, dien_tich = getCircle(R)
print("Chu vi hình tròn là:", round(chu_vi, 2))
print("Diện tích hình tròn là:", round(dien_tich, 2))
