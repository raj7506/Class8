def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)
def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i + 1]
    a[a_size-1] = temp

def printarray(a, a_size):
    for i in range(a_size):
        print("% d"% a[i])
    print("\n")

a = [12,12,13,98,5,32,982]
printarray(a,len(a))
rotations(a, 2, len(a))
printarray(a, len(a))