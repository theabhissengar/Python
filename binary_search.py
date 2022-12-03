def binarysearch(arr,low,high,x):
    if high>=low:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid

        elif arr[mid]>x:
            return binarysearch(arr, low,mid-1,x)
        else:
            return binarysearch(arr,mid+1,high,x)
    else:
        return -1



arr=[2,3,10,40,18,6,9]
x=int(input("Enter the number to be SEARCH: "))
element=binarysearch(arr,0,len(arr)-1,x)
if element!=-1:
      print("Element is present at index: ",str(element))
else:
    print("Element is not present in the array")
