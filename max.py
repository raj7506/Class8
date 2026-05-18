def maxelement(a):

    length = len(a)

    if length == 1:
        return a[0]
    return max(a[0], maxelement(a[1:]))

a = [1, 2, 632, 1726, 90, 100]

print("Largest element is: ", maxelement(a))