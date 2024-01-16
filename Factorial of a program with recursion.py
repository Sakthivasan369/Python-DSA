def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
number=int(input("Enter the factorial of a number:"))
if number==0:
    print("The factorial of 0 is 1")
elif number<0:
    print("The factorial of negative numbers does not exist")
else:
    print(f"The factorial of this number is {fact(number)}")
------------------------------------------------------------------------
Output
Enter the factorial of a number:7
The factorial of this number is 5040
