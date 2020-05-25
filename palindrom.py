n=str(input("enter a number"))
r=0
r=n
while(n!=0):
    r=n%10
    r=r*10+r
if(t==r):
    print("palindrome")
else:
    print("not a palindrome")
