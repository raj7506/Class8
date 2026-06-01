def print2largest(a, a_size):
    largest = second_largest = -2147483648
    for i in range(a_size):
        if(a[i] > largest):
            second_largest = largest
            largest = a[i]
        elif(a[i] > second_largest and a[i] != largest):
            second_largest = a[i]

    print(second_largest)

a = [1,2,3,4,5,6,7,8,9]
a_size = len(a)
print2largest(a, a_size)