def quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
    return arr
def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
if __name__=="__main__":
    arr=[10,40,30,50,60,20]
    print("Before Sorting")
    for y in arr:
        print(y,end=" ")
    res=quick_sort(arr,0,len(arr)-1)
    print("\nAfter Sorting")
    for x in res:
        print(x,end=" ")
---------------------------------------------------------------------------------------------------------------------------------------
Output
Before Sorting
10 40 30 50 60 20 
After Sorting     
10 20 30 40 50 60
