l=[]
n=int(input("Enter number of elements:"))
print("Enter the elments of the lsit")
for elt in range(n):
    elt=int(input())
    l.append(elt)
print("List is ",l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("Sorted List is :",l)
-----------------------------------------------------------------
Output
Enter number of elements:5
Enter the elments of the lsit
23
47
89
43
12
List is  [23, 47, 89, 43, 12]
Sorted List is : [12, 23, 43, 47, 89]


