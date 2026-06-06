def leaders(a, a_size):
    current_max = a[a_size-1]
    print(current_max)

    for i in range(a_size-2, -1, -1):
        if current_max < a[i]:
            print(a[i])

a = [16, 17, 4, 3, 5, 354]
leaders(a, len(a))