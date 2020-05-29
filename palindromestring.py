string = input("Please enter String : ")
print(string[:: - 1])
if(string == string[:: - 1]):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")
