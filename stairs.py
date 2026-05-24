def way(stairs):
    if stairs<0:
        return 0
    if stairs==0:
        return 1
    twoSteps = 0
    oneStep = 0

    if (stairs>=0):
        twoSteps = way(stairs-2)
    oneStep = way(stairs-1)

    return twoSteps + oneStep
stairs = int(input("Enter number of steps: "))
print("Number of ways to climb", way(stairs))