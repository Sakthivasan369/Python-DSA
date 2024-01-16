def print_reverse_of_string_if_length_is_3(string):
    elements=len(string)
    
    if elements%3==0:
        reversed_string=string[::-1]
        return reversed_string
    else:
        return string
string=input("Enter the string : ")
res=print_reverse_of_string_if_length_is_3(string)
print(f"The string is {res}")
--------------------------------------------------------------
Output
Enter the string : cak
The string is kac
---------------------------------------------------------------
Output 2
Enter the string : giraffe
The string is giraffe
