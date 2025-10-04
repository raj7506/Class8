num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
avg = num1 + num2 + num3/3
if avg>num1 and avg>num2 and avg>num3:
    print("%d is higher %d,%d,%d"%(avg,num1, num2, num3))
elif avg>num1 and avg>num2:
    print("%d is higher %d,%d"%(avg,num1, num2))
elif avg>num1 and avg>num3:
    print("%d is higher %d,%d"%(avg, num1, num3))
elif avg>num2 and avg>num3:
    print("%d is higher %d,%d"%(avg, num2, num3))
elif avg>num1:
    print("%d is just higher than %d"%(avg,num1))
elif avg>num2:
    print("%d is just higher than %d"%(avg,num2))
elif avg>num3:
    print("%d is just higher than %d"%(avg,num3))
else:
    print("Invalid input")