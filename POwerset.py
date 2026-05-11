def printPowerSet(s, set_size):
    power_set_size = 2**set_size

    for outer in range(power_set_size):
        subset = []

        for inner in range(set_size):
            if outer & (1<<inner)>0:
                subset.append(s[inner])

        print(subset)

set_elements = [1,2,3]
set_size = len(set_elements)
printPowerSet(set_elements, set_size)