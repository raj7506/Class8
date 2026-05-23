n = int(input("Enter your number: "))

def checknpower(n):
    if(n<=0):
        return False
    
    if(n==1):
        return True
    if(n%4==0):
        return checknpower(n/4)
    return False

if(checknpower(n)):
    print("Power of 4")
else:
    print("Not a power of 4")