import calendar
date=input("Enter the date by separating it with (-):")
d,m,y=date.split("-")
print("The month full name:",calendar.month_name[int(m)])
print("The month abbreviation:",calendar.month_abbr[int(m)])
-------------------------------------------------------------------------------
Output
Enter the date by separating it with (-):15-08-1947
The month full name: August
The month abbreviation: Aug
