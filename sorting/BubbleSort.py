def bubble_sort(arr):
    lenght = len(arr)
    for i in range(lenght-1):
        changed = 1
        for j in range(lenght-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changed = 0
        if(changed):
            break


# array = [8,7,2,1,5,3,9,5,3]
# print(array)
# bubble_sort(array)
# print(array)