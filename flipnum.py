def flip(num1, num2):
    xor = num1 ^ num2
    flip_count = bin(xor).count('1')
    return flip_count

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("Number of flips needed:", flip(num1, num2))