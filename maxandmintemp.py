#Minimum element
def minimumelement(a,size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp

#Maximum element
def maximumelement(a,size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
    return temp

a = [12, 1234, 45, 76, 1]
size = len(a)
print("Maximum element of array is", maximumelement(a, size))
print("Minimum element of array is", minimumelement(a, size))