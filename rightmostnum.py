def rightmost_set_bit(number):

    if number == 0:
        return 0

    return number & -number


number = int(input("Enter a number: "))

result = rightmost_set_bit(number)

print("Rightmost set bit:", result)