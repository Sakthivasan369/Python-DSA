def additon(a,b):return a+b
def subraction(a,b):return a-b
def multiplication(a,b):return a*b
def division(a,b):  return a/b if b!=0 else "Cannot divide by 0 "
print("1.ADDITION OPERATION ")
print("2.SUBRACTION OPERATION")
print("3.MULTIPLICATION OPERATION")
print("4.DIVISION OPERATION")
operations={1:additon,
            2:subraction,
            3:multiplication,
            4:division}
choice=int(input("Enter your choice 1-4 :"))
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if choice in operations:
    result=operations[choice](num1,num2)
    print(f"The result is{result}")
else:
    print("Invalid Choice")
  ---------------------------------------------------------------------------
Output 1
1.ADDITION OPERATION 
2.SUBRACTION OPERATION    
3.MULTIPLICATION OPERATION
4.DIVISION OPERATION      
Enter your choice 1-4 :4  
Enter the first number:23
Enter the second number:0
The result isCannot divide by 0 
-----------------------------------------------------------------------------
Output 2
1.ADDITION OPERATION 
2.SUBRACTION OPERATION    
3.MULTIPLICATION OPERATION
4.DIVISION OPERATION      
Enter your choice 1-4 :3  
Enter the first number:23
Enter the second number:3
The result is69 
-------------------------------------------------------------------------------
Output 3
1.ADDITION OPERATION 
2.SUBRACTION OPERATION    
3.MULTIPLICATION OPERATION
4.DIVISION OPERATION      
Enter your choice 1-4 :2  
Enter the first number:23
Enter the second number:45
The result is-22
----------------------------------------------------------------------------------
Output 4
1.ADDITION OPERATION 
2.SUBRACTION OPERATION    
3.MULTIPLICATION OPERATION
4.DIVISION OPERATION      
Enter your choice 1-4 :1  
Enter the first number:23
Enter the second number:45
The result is68
















