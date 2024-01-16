def find_third_largest(numbers):
    sorted_numbers=sorted(numbers,reverse=True)
    if len(sorted_numbers)>=3:
        return sorted_numbers[2]
    else:
        print("The list  should contain  atleast 3  numbers")
numbers=[int(x) for x in input("Enter the numbers separated by space ").split()]
result=find_third_largest(numbers)
print(f"The third largest number is {result}")
----------------------------------------------------------------------------------------------------
Output
Enter the numbers separated by space 23 4 56 754 3 1 2 34 5 654 
The third largest number is 56
