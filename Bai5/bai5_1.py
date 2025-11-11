print ("Sinh vien: Hoang Vo Khac Quan")
print ("Ma so sv: 245752021610150")
## File: mymath.py ##
def square(n):
    return n*n
def cube(n):
    return n*n*n
def average(values):
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
    return float(sum)/nvals

## My script using the math module ##

values = [2,4,6,8,10]
print('Squares:')
for v in values:
    print(square(v))
print ('Cubes:')
for v in values:
    print(cube(v))
print('Average: ' + str(average(values)))

print(square(2))
print(square(3))
