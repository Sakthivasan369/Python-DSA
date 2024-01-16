test_tup=tuple(input("Enter The elements of the tuple :").split())
print("The Original tuple is :",(test_tup))
res=tuple(set(test_tup))
print(f"The tuple after removing duplicates :{(res)}")
----------------------------------------------------------
Output
Enter The elements of the tuple :201 202 a 202 b ab 201
The Original tuple is : ('201', '202', 'a', '202', 'b', 'ab', '201')
The tuple after removing duplicates :('202', 'a', 'b', '201', 'ab')

