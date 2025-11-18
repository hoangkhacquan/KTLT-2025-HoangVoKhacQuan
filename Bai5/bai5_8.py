print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i  
    return False, -1   
arr = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
result = Sequential_Search(arr, 31)
print(f"Kết quả: {result}") 
if result[0]:
    print(f"Tìm thấy {31} tại chỉ số: {result[1]}")
else:
    print(f"Không tìm thấy")
