a = 5
b = 8

a1 = bin(a).count('1')
b1 = bin(b).count('1')

if a1>b1:
    print(a, "is greater than", b)
else:
    print(b, "is greater than", a)