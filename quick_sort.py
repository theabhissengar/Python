def Partition(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]

    return (i+1)


def Quicksort(arr,low,high):
    if low<=high:
        pi=Partition(arr,low,high)
        Quicksort(arr,low,pi-1)
        Quicksort(arr,pi+1,high)



arr=[1,7,4,2,9,18,1,-2,68,-24]
print("Unsorted array: ",arr)
size=len(arr)
Quicksort(arr,0,size-1)
print('Sorted array in ascending order is: ',arr)
