r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))
m=[]
for i in range(r):
    l=[]
    for i in range(c):
       v=int(input()) 
       l.append(v)
    m.append(l)
print(m)
-----------------------------------------------------------------
Output:
Enter the number of rows:2
Enter the number of columns:2
1 
2
3
4
[[1, 2], [3, 4]]
-----------------------------------------------------------------
Output 2:
Enter the number of rows:4
Enter the number of columns:3
1
2
3
4
5
6
7
8
9
10
11
12
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
