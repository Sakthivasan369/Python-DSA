mylist=list(map(int,input("Enter the elements of the list (separated by space):").split()))
print("List before rotation:",mylist)
n=int(input("Number of times the list has to be rotated:"))
if n>len(mylist):
    n=int(n%len(mylist))
mylist=(mylist[-n:]+mylist[:-n])
print("Updated List after rotation:",mylist)
----------------------------------------------------------------------------------------------------------
Output
Enter the elements of the list (separated by space):5 20 34 67 89 94 98 110
List before rotation: [5, 20, 34, 67, 89, 94, 98, 110]
Number of times the list has to be rotated:4
Updated List after rotation: [89, 94, 98, 110, 5, 20, 34, 67]
