def selection_sort(arr):
    lenght = len(arr)
    for i in range(lenght-1):
        max = i
        for j in range(i+1, lenght):
            if arr[j] < arr[max]:
                max = j
        arr[i], arr[max] = arr[max], arr[i]


# array = [4,3,1,7,2]
# print(array)
# selection_sort(array)
# print(array)