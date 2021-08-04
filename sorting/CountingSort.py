def counting_sort(arr):
    n = len(arr)
    Max = max(arr)

    keys = [0]*(Max+1)
    sorted = [0]*n

    for i in range(n):
        keys[arr[i]] += 1

    for i in range(1,Max+1):
        keys[i] += keys[i-1]

    for i in range(n):
        sorted[keys[arr[i]]-1] = arr[i]
        keys[arr[i]] -=1

    return sorted


array = [5,2,1,7,1,9,4,2]
print(array)
print(counting_sort(array))