def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i-1
        while (j >= 0 and arr[j] > val):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val
        
    return arr

    
# array = [4,3,1,7,2,2]
# print(array)
# insertion_sort(array)
# print(array)