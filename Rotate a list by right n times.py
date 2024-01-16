def rotate(l,order):
    for i in range(0,order):
        j=len(l)-1
        while j>0:
            temp=l[j]
            l[j]=l[j-1]
            l[j-1]=temp
            j-=1
        print(i,'rotation',l)
l=list(map(int,input("Enter the numbers to be rotated:").split()))
n=int(input("Number of times the list has to be rotated:"))
rotate(l,n)
-----------------------------------------------------------------------------------------
Output
Enter the numbers to be rotated:1 2 3 4 5 
Number of times the list has to be rotated:3
0 rotation [5, 1, 2, 3, 4]
1 rotation [4, 5, 1, 2, 3]
2 rotation [3, 4, 5, 1, 2]


