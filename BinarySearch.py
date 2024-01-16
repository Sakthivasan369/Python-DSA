def BinarySearch(arr,low,high,search_element):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==search_element:
            return mid
        elif arr[mid]>search_element:
            return BinarySearch(arr,low,mid-1,search_element)
        else:
            return BinarySearch(arr,mid+1,high,search_element)
    else:
        return -1
arr=list(map(int,input("Enter the elements : ").split(" ")))
search_element=int(input("Enter the element to search:"))
result=BinarySearch(arr,0,len(arr)-1,search_element)
if result!=-1:
    print(f"Element found at index:{result}")
else:
    print("Element not found in the array SORRY!")
----------------------------------------------------------------------------
Output
Enter the elements : 12 23 25 36 47 58 69 70 89 91 102
Enter the element to search:58
Element found at index:5








