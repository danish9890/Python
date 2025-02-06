def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
n=int(input("Enter the Number "))
print(sum(n))

def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)
n=int(input("enter the number "))
pattern(n)

print("w222")
