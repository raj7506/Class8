def pushzerotoend(a,a_size):
    zero = 0
    nonzero = 0
    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero] = a[zero],a[nonzero]
            zero += 1
        nonzero+=1

a =[1,0,2,3,6,0,0,0,23,913,124]
a_size = len(a)
print(a)
pushzerotoend(a, a_size)
print("Array after pushing all zeros to end of array:")
print(a)