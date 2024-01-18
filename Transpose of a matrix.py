r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))
m=[]
for i in range(r):
    l=[]
    for i in range(c):
       v=int(input()) 
       l.append(v)
    m.append(l)
print("The matrix is given by :")
for i in range(r):
    for j in range(c):
        print(m[i][j],end =" ")
    print()
trans=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(c):
        trans[j][i]=m[i][j]
print("The transpose of the given matrix is :")
for i in range(r):
    for j in range(c):
        print(trans[i][j],end=" ")
    print()
------------------------------------------------------------------------
Output 1
Enter the number of rows:2
Enter the number of columns:2
5
6
7
8
The matrix is given by :
5 6 
7 8 
The transpose of the given matrix is :
5 7 
6 8
-------------------------------------------------------------------------------
Output 2
Enter the number of rows:3
Enter the number of columns:3
9
8
7
5
6
7
8
7
6
The matrix is given by :
9 8 7 
5 6 7 
8 7 6 
The transpose of the given matrix is :
9 5 8 
8 6 7 
7 7 6 
