def check_voter_age(age):
    if age>=18:
        print("You're eligible to vote")
    else:
        raise ValueError("Invalid Age! you're not eligible to vote")
try:
    age=int(input("Enter your age :"))
    check_voter_age(age)
except ValueError as e:
    print(e)
-------------------------------------------------------------------------------------------------
Output
Enter your age :23
You're eligible to vote
-------------------------------------------------------------------------------------------------
Output 2
Enter your age :14
Invalid Age! you're not eligible to vote
  
