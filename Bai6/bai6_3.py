print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
class Nguoi:
    def getGender(self):
        return "Unknown"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
aNam = Nam()
aNu = Nu()
print(aNam.getGender())  
print(aNu.getGender())   
