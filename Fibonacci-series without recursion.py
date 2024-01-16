first_num=int(input("Enter the first no:"))
second_num=int(input("Enter the second num:"))
num_of_terms=int(input("Enter the number of terms...."))
print(f"The fibonacci series of the numbers{first_num} and {second_num}")
while(num_of_terms-2):
    third_num=first_num+second_num
    first_num=second_num
    second_num=third_num
    print(third_num)
    num_of_terms=num_of_terms-1
----------------------------------------------------------------------------------------------------
Output
The fibonacci series of the numbers 1 and 13
14
27
41
68
109
177
286
463
