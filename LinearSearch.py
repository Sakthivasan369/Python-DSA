def linearSearch(list1,n,key):
    for i in range(0,n):
        if(list1[i]==key):
            return i
    return-1
list1=list(map(int,input("Enter The numbers:").split(" ")))
key=int(input("Enter the element to search:"))
n=len(list1)
res=linearSearch(list1,n,key)
if res==-1:
    print("Element not found ")
else:
    print(f"Element found at index:{res}")
--------------------------------------------------------------------------
Output
Enter The numbers:43 32 31 35 89 65 44
Enter the element to search:31
Element found at index:2
