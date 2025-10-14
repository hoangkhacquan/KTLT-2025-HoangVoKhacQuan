print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
str=input("Enter a String:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)
