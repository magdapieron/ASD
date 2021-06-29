def heapify(arr, size, i): #size - heap size, i - parent's index
    index = i
    left_child = i*2+1
    right_child = i*2+2

    if(left_child < size and arr[left_child] > arr[index]):
        index = left_child
    if(right_child < size and arr[right_child] > arr[index]):
        index = right_child
    if index != i:
        arr[i], arr[index] = arr[index], arr[i]
        heapify(arr, size, index)

def heap_sort(arr):
    size = len(arr)

    for i in range (size//2-1, -1, -1):
        heapify(arr, size, i)

    for i in range (size-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# array = [4,3,1,7,2,1,8,3]
# print(array)
# heap_sort(array)
# print(array)