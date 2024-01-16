n=int(input("ENter number of elements:"))
print("Enter the elements of the list:")
L=[]
for elt in range(n):
    elt=float(input())
    L.append(elt)
print("List is ",L)
for i in range(len(L)):
    for j in range((len(L)-1)-i):
        if L[j]>L[j+1]:
            temp=L[j]
            L[j]=L[j+1]
            L[j+1]=temp
print("Sorted LISt is :",L)
--------------------------------------------------------------------------
Output
ENter number of elements:6
Enter the elements of the list:
23
234 
2340
23.4
2.34
0.23
List is  [23.0, 234.0, 2340.0, 23.4, 2.34, 0.23]
Sorted LISt is : [0.23, 2.34, 23.0, 23.4, 234.0, 2340.0]
