l=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements of the list:")
for elt in range(n):
    elt=int(input())
    l.append(elt)
print("List is ",l)
for i in range(len(l)):
    for j in range(0,i):
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("Sorted List is ",l)
-----------------------------------------------------------------------------------------
Output
Enter the number of elements:5
Enter the elements of the list:
12          
23   
45 
76 
03
List is  [12, 23, 45, 76, 3]       
Sorted List is  [3, 12, 23, 45, 76]
