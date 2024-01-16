def recur_fibo(number):
    if number<=1:
        return number
    else:
        return (recur_fibo(number-1)+recur_fibo(number-2))
nterms=int(input("Enter the number for Fibonacci Series :"))
if nterms<=0:
    print("Please enter a positive integer ")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(recur_fibo(i),end=" ")
      ------------------------------------------------------------------------------
Output
Enter the number for Fibonacci Series :20
Fibonacci Sequence:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
