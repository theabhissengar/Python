def linearsearch(arr,n,x):
    for i in range(0,n):
        if(arr[i]==x):
            return i
    return -1


arr=[2,4,0,1,9,12]
x=int(input("Enter the number to be SEARCH: "))
n=len(arr)
element=linearsearch(arr,n,x)
if(element==-1):
    print("Element not found")
else:
    print("Element is found at index:",element)
