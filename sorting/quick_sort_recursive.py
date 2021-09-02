def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left,right):
        if arr[j] <= pivot :           
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    arr[i], arr[right] = arr[right], arr[i]
    return i


def sort(arr, left, right):
    if(left<right):
        pivot = partition(arr,left,right)
        sort(arr, left, pivot-1)
        sort(arr, pivot, right)


def quick_sort(arr):
    sort(arr,0,len(arr)-1)


# array = [1,7,2,4,3,5]
# print(array)
# quick_sort(array)
# print(array)