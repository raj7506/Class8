def reverse_bits(number, bits=32):
    reversed_num = 0

    for i in range(bits):

        reversed_num <<= 1

        reversed_num |= (number & 1)

        number >>= 1

    return reversed_num


number = int(input("Enter a number: "))

result = reverse_bits(number)

print("Reversed bit number:", result)