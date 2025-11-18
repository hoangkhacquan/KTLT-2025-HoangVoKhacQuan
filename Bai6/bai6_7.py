print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def circumference(self):
        return 2 * math.pi * self.radius
if __name__ == "__main__":
    r = float(input("Nhập bán kính hình tròn: "))
    circle = Circle(r)
    print("Diện tích hình tròn:", circle.area())
    print("Chu vi hình tròn:", circle.circumference())
