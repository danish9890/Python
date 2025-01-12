n=int(input("enter "))
for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1) ,end="")
    print("")

num=int(input("enter a number "))
product=1
for i in range (1,num+1):
    product=product *i
print(f"the factorial  {num} is {product}")
