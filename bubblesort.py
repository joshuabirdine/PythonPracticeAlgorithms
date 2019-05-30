def bubbleSort(arr):
    for nextnum in range(len(arr)-1,0,-1):
        for i in range(nextnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

                              
arr = [9, -3, 3, 2, 1, 0]
print("Original input:")
print(arr)
bubbleSort(arr)
print("BubbleSorted:")
print(arr)