def selectionsort(arr,size):
    for index in range(size):
        min_index=index
        
        for j in range(index + 1, size):
            if arr[j]<arr[min_index]:
                min_index=j
        (arr[index],arr[min_index])=(arr[min_index],arr[index])

arr=[-2,45,0,11,-9,88,-97,-202,707]
size=len(arr)
selectionsort(arr,size)
print("The array after sorting is:")
print(arr)
